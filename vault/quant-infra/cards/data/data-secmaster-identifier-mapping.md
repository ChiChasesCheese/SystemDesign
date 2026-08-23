---
id: data-secmaster-identifier-mapping
node: data.security-master
type: qa
---
## Q
Your security master needs to map one instrument across CUSIP, ISIN, and FIGI so it can join data from three vendors who each use a different scheme. Which of the three, if any, can you safely treat as immutable and never reused — and what breaks if you assume all three are?

## A
**Only FIGI (Financial Instrument Global Identifier) is designed to be permanent and never reassigned; CUSIP and ISIN are not.** A CUSIP (issued by CUSIP Global Services, US/Canada-scoped) is tied to a specific issuer-and-issue combination and **can change** on corporate actions that alter the legal issuer — a merger, a reincorporation, sometimes even a name change — with the old CUSIP potentially reused years later for an unrelated issue. An ISIN simply wraps a country code and a local identifier (often the CUSIP itself for US securities) plus a check digit, so it inherits every one of CUSIP's mutability problems for US names, while adding cross-border ambiguity: the same economic security can carry different ISINs in different listing countries (a dual-listed stock), so "one ISIN = one company" is also false. FIGI, by contrast, is issued for free by the Object Management Group / OpenFIGI, is never reused even when an instrument is delisted, and is granular enough to assign a distinct identifier per venue/listing — the property the other two lack.

Assuming immutability of CUSIP/ISIN causes exactly the ticker-reuse failure mode one level up the stack: a corporate action silently changes the identifier your mapping table has cached as "the" key for an instrument, and joins against stale CUSIP/ISIN values either drop the instrument entirely or, worse, match it to whatever unrelated issue later reused the old code. A robust security master resolves external identifiers *through* an internal permanent key (often FIGI or an internal surrogate) with effective-dated mapping rows, exactly as it does for tickers — never uses CUSIP/ISIN as the primary key.

## Q zh
你的证券主数据需要把一个标的映射到 CUSIP、ISIN、FIGI 三种编码体系上，以便拼接三家各自使用不同体系的供应商数据。这三者里，哪一个（如果有的话）可以放心当作永不改变、永不复用的？如果把三者都当成如此会出什么问题？

## A zh
**只有 FIGI（Financial Instrument Global Identifier）被设计为永久且从不重新分配；CUSIP 和 ISIN 都不是。** CUSIP（由 CUSIP Global Services 发放，覆盖美国/加拿大）绑定的是特定的发行人-发行组合，在改变法定发行人的公司行为（并购、重新注册地，有时甚至改名）发生时**可能改变**，而旧的 CUSIP 有可能在若干年后被回收给一个不相关的新发行使用。ISIN 本质上只是在国家代码加本地标识符（对美国证券而言，本地标识符往往就是 CUSIP 本身）之外再加一位校验码，所以它对美国标的继承了 CUSIP 的全部可变性问题，还额外带来跨境歧义：同一只经济上的证券在不同上市国家可能持有不同的 ISIN（双重上市股票），所以"一个 ISIN 对应一家公司"同样不成立。相比之下，FIGI 由 Object Management Group / OpenFIGI 免费发放，即便标的退市也从不复用，而且颗粒度足够细，可以为每个交易场所/上市地分配一个独立标识符——这是另外两者都不具备的特性。

假设 CUSIP/ISIN 不可变，会在上一层堆栈里精确重演股票代码复用的那种故障：一次公司行为悄悄改变了映射表里已经缓存为"该标的的键"的标识符，之后按旧的 CUSIP/ISIN 做连接，要么完全丢失该标的，要么更糟——把它匹配到后来复用了这个旧代码的、毫不相关的另一个发行上。一个健壮的证券主数据会**通过**一个内部永久键（通常是 FIGI 或内部代理键）来解析外部标识符，用带生效日期的映射行来记录，正如它对股票代码所做的那样——绝不会把 CUSIP/ISIN 当作主键。
