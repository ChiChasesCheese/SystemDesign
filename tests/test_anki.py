from trellis.anki import align
from trellis.skeleton import load_skeleton

SKELETON = """
domain: demo
title: Demo
nodes:
  - id: alpha
    order: 7
    title: Alpha
    children:
      - id: alpha.one
        title: One
"""


class FakeAnki:
    """Collection with one mis-decked card and one stale empty deck."""

    def __init__(self):
        self.decks = {
            "Demo::01 Alpha::One": [],          # stale ordinal, now empty
            "Demo::07 Alpha": [101],            # card sitting on the branch deck
            "Demo::07 Alpha::One": [],
        }
        self.tags = {101: "demo::alpha::one"}
        self.calls = []

    def __call__(self, action, url, **params):
        self.calls.append(action)
        if action == "findCards":
            q = params["query"]
            if q.startswith("tag:"):
                tag = q.split()[0][len("tag:"):]
                exclude_deck = q.split('-deck:"')[1].rstrip('"')
                return [cid for cid, t in self.tags.items()
                        if t == tag and cid not in self.decks.get(exclude_deck, [])]
            deck = q.split('deck:"')[1].rstrip('"')
            return [cid for name, cards in self.decks.items()
                    if name == deck or name.startswith(deck + "::")
                    for cid in cards]
        if action == "createDeck":
            self.decks.setdefault(params["deck"], [])
            return None
        if action == "changeDeck":
            for cards in self.decks.values():
                for cid in params["cards"]:
                    if cid in cards:
                        cards.remove(cid)
            self.decks[params["deck"]].extend(params["cards"])
            return None
        if action == "deckNames":
            return list(self.decks)
        if action == "deleteDecks":
            for name in params["decks"]:
                del self.decks[name]
            return None
        raise AssertionError(f"unexpected action {action}")


def test_align_moves_cards_and_deletes_stale_decks(tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text(SKELETON, encoding="utf-8")
    skeleton = load_skeleton(path)
    fake = FakeAnki()

    result = align(skeleton, call=fake)

    assert result["moved"] == 1
    assert fake.decks["Demo::07 Alpha::One"] == [101]
    # stale ordinal deck gone; current decks (with cards beneath) kept
    assert "Demo::01 Alpha::One" not in fake.decks
    assert "Demo::07 Alpha" in fake.decks


def test_align_noop_on_clean_collection(tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text(SKELETON, encoding="utf-8")
    skeleton = load_skeleton(path)
    fake = FakeAnki()
    align(skeleton, call=fake)
    calls_before = len(fake.calls)
    result = align(skeleton, call=fake)
    assert result["moved"] == 0 and result["deleted"] == []
    assert len(fake.calls) > calls_before  # it did re-check, found nothing
