---
id: quality-divergent-vs-shotgun
node: quality.smells
type: qa
---
## Q
Divergent change vs shotgun surgery — both are change preventers. Distinguish them and give each one's fix.

## A
They're mirror images, defined by the mapping between *reasons to change* and *classes touched*:

- **Divergent change**: **one class, many reasons** — every new pricing rule, every new report format, every DB tweak all edit the same class. Fix: **extract class** — split by responsibility so each class has one reason to change (SRP).
- **Shotgun surgery**: **one reason, many classes** — adding a currency means small edits in 12 files. Fix: **move method/field** to consolidate the scattered behavior into one class (or introduce the missing abstraction that owns it).

Memory hook: divergent = too much *converges into* one class; shotgun = one change *sprays across* many.

## Q zh
Divergent Change 和 Shotgun Surgery 之间有什么区别？

## A zh
**Divergent Change（发散式变化）**：
- 一个类因多个不相关的原因而改变
- 例子：支付处理器处理信用卡、PayPal 和加密货币
```
新的支付方式 ➜ 修改支付处理器
税法改变 ➜ 修改支付处理器
```
- 类有多个理由改变（违反 SRP）

**Shotgun Surgery（猎枪式修改）**：
- 一个改变需要修改许多类
- 例子：添加新的日志级别需要修改 10 个类
```
新的日志级别 ➜ 修改 Logger、ConsoleWriter、FileWriter、...
```
- 变化分散在许多地方，难以找到所有地方

解决方案：
- Divergent：拆分类（提取不同的原因到不同的类）
- Shotgun：将分散的代码聚集在一个地方（移动方法、提取类）
