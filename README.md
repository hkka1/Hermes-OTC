# Hermes-OTC (赫尔墨斯) ⚖️
**The First LLM-Driven Autonomous OTC Escrow Agent on OKX Onchain OS**

## 1. 赛道宣言：让交易回归对话
Web3 的大额场外交易（OTC）充斥着信任危机与繁琐的担保流程。Hermes 旨在打破这一僵局。它不仅是一个基于 OKX X Layer 的智能合约，更是一个能够听懂人类讨价还价的 AI 谈判官与执行体。
无需看懂复杂的 DEX 界面，买卖双方只需使用自然语言进行沟通，Hermes 将自动捕捉共识，并执行毫秒级的链上清算。

## 2. 核心架构与工作流
1. **The Negotiation Room (去中心化谈判室):** 买卖双方通过签名进入加密聊天通道。
2. **Semantic Consensus (语义共识监听):** 基于 LLM 的 Hermes 引擎实时分析聊天流。当检测到双方达成“成交 (Deal)”意图时，自动冻结对话。
3. **Intent Extraction (意图抽取):** LLM 将冗长的讨价还价转化为精确的 JSON 格式金融指令（如 `{"Alice_pays": "1000 USDC", "Bob_pays": "50000 PEPE"}`）。
4. **Atomic Swap (Trade Kit 原子交换):** 双方通过 Web3 钱包确认意图后，Hermes 唤醒 **OKX Agent Trade Kit**，在 X Layer 上同时锁定双方资产，并执行去信任化的原子交换。

## 3. 系统交互图


## 4. 终端复现指南 (实机模拟)
```bash
git clone [https://github.com/YourName/Hermes-OTC.git](https://github.com/YourName/Hermes-OTC.git)
cd Hermes-OTC
pip install -r requirements.txt
# 启动 Hermes AI 担保谈判室模拟器
python run_hermes_room.py
```
