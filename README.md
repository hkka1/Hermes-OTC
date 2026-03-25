# Hermes-OTC (赫尔墨斯) ⚖️
```mermaid
graph TD
    subgraph Web3_Dark_Forest [加密黑暗森林 外部环境]
        A[Alice Wallet]
        B[Bob Wallet]
    end

    subgraph Hermes_Tribunal [Hermes AI 仲裁核心 TEE隔离区]
        C{去中心化加密谈判室 WSS}
        D[Blue Agent: LLM 语义提取引擎]
        E[Red Agent: 欺诈/毒性扫描器]
        F[[结构化金融意图 JSON]]
    end

    subgraph OKX_X_Layer [OKX Onchain OS 结算层]
        G[OKX Agent Trade Kit]
        H[(Hermes Escrow Vault 合约)]
        I((原子交换 Atomic Swap))
    end

    %% 数据流向图
    A <-->|自然语言博弈| C
    B <-->|自然语言博弈| C
    
    C -->|实时流监听| D
    D -->|提取币种金额| F
    C -->|旁路安全审计| E
    
    E -- 安全阈值 > 99.9% --> F
    F -->|唤醒底层执行体| G
    
    G -->|多重签名授权| H
    H -->|双向锁定资产| I
    
    I -->|零信任清算| A
    I -->|零信任清算| B

    classDef core fill:#000,stroke:#00ff66,stroke-width:2px,color:#00ff66;
    classDef safe fill:#0b1021,stroke:#00aaff,stroke-width:1px,color:#fff;
    class C,D,E,F safe;
    class G,H,I core;
```
**The First LLM-Driven Autonomous OTC Escrow Agent on OKX Onchain OS**

## 1. 赛道宣言：让机器经济回归去信任化中介
人类擅长欺骗，但代码不会。在 Web3 的黑暗森林里，场外交易（OTC）充斥着信任危机与繁琐的担保流程。
Hermes-OTC 不是一个简单的交易代理，它是一个由微调 LLM 驱动的永不宕机的 AI 裁决者。它活在加密聊天室里，听懂讨价还价，并将非结构化对话瞬间转化为确定性的链上金融结算。我们在 OKX X Layer 上构建了属于机器经济时代的无信任资本流转。

## 2. 核心架构与“Tribunal”风控体系

Hermes 摒弃了单体 Agent 的单点故障，独创了 **红蓝对抗多智能体法庭 (Tribunal)**：

* **Blue Agent (研判引擎):** 基于微调的 `gpt-4-turbo` 或 `llama-3-70b`，负责从聊天记录中提取 `[币种]`、`[数量]`、`[价格]` 的 JSON 结构化金融意图。
* **Red Agent (毒性/欺诈扫描器):** 专门用来“找茬”的安全模型。它**只做一件事：寻找“伪复杂代码”、“冗余逻辑炸弹”和“刷分特征”**。
* **The Kill Switch ( Trade Kit):** 只有当置信度 > 99.8% 且红 Agent 判定“欺诈概率 < 0.1%”时，才会唤醒 **OKX Agent Trade Kit**，执行去信任化的原子交换。

## 3. 终极执行生命周期 (A2A 序列图)

```mermaid
sequenceDiagram
    autonumber
    participant Alice as 👨‍💻 开发者 A (Seller)
    participant Bob as 📈 开发者 B (Buyer)
    participant ChatRoom as 📡 谈判聊天室 (WSS)
    participant HermesAI as 🧠 Hermes AI (TEE)
    participant TradeKit as ⚙️ OKX Trade Kit
    participant Vault as 🔐 X Layer Vault
    
    Alice->>ChatRoom: 发送 "我有 50k 土狗币，换 900U"
    activate ChatRoom
    Bob->>ChatRoom: 发送 "Deal，900U。"
    deactivate ChatRoom
    
    Note over HermesAI: --- 阶段一：Millisecond-level 数据分析 ---
    
    HermesAI->>HermesAI: 1. Clone 源码并提取意图
    activate HermesAI
    
    Note over HermesAI, TradeKit: --- 阶段二：红蓝对抗 (Tribunal) 决策 ---
    
    HermesAI->>HermesAI: 2. 毒性/欺诈扫描 (Score 1/100)
    HermesAI->>HermesAI: 3. 创新度评分 (92/100) (Passed)
    
    Note over HermesAI, TradeKit: --- 阶段三：OKX Onchain OS 最终执行 ---
    
    HermesAI->>TradeKit: 4. 触发投资指令 (Inject Seed Funding)
    activate TradeKit
    
    TradeKit->>Vault: 5. 构建交易: 质押 10,000 USDC
    TradeKit-->>HermesAI: 6. 返回 Tx Hash (Tx: 0xDEADBEEF...)
    deactivate TradeKit
    
    HermesAI-->>Alice: 7. 投资完成！ TxHash 已上链。
    deactivate HermesAI
```

## 4. 终端复现指南 (实机模拟) & 零成本本地沙盒

我们深知物理网络的复现壁垒。为此，本项目独创了 **`LOCAL_MOCK` (本地暗影沙盒模拟层)**。评委只需在普通笔记本上运行该模拟器，即可零成本、零延迟地体验 AI Agent 抓取黑客攻击、并在毫秒内完成 MEV 抢跑拦截的全套底层逻辑。

```bash
# 1. 安装依赖
pip install websockets colorama okx_agent_trade_kit

# 2. [终端 1] 启动本地 Mock 节点 (模拟内存池与黑客攻击)
python mock_env/shadow_mempool_mock.py

# 3. [终端 2] 启动 Aegis Agent 接入本地虚拟节点进行毫秒级防守
python core/start_aegis_node.py --mode LOCAL_MOCK --rpc ws://localhost:8546
```
*(注：物理壁垒已被击碎，复现门槛已降至一台普通的笔记本电脑。)*

## 5. 企业级工程组件
* 📁 `core/`: 内部“Tribunal”双 AI 引擎
* 📁 `onchain/`: `okx_agent_trade_kit` 交互库
* 📁 `contracts/`: `HermesEscrowVault.sol` 智能合约
