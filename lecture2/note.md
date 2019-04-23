### Models,Policy,Values的定义？
- Models:??
- Policy: 将状态映射为action的函数。
- Value function:?? 

### Markov Process
- 文字描述：给定现在，将来与过去无关。具有无记忆性。
- 数学公式：$p(s_{t+1}|s_t,a_t)=p(s_{t+1}|h_t,a_t)},h_t=s_0,a_0,s_1,a_1,...$
- 定义：状态集合S；转移矩阵P。
### Markov Reward Process(MRP)
- 定义：具有reward的马尔科夫链。(markov chain + reward)

### Horizon
- 定义：一个episode中的步数（视野范围）
### Return,G_t
- 定义：每一步的reward的加权就和。
- G_t = r_t + {\gama}r_{t+1}+{\gama}^2r_{t+2}+...

### 状态值函数(State Value Function)
- 定义：V(s)=E[G_t|S_t=s]

### Markov Decision Process(MDP)
- 定义：MDP是一个5元组(S,A,P,R,\gama)
- 具有action的MRP
- 具有以下几个特征：
- S：状态集合。
- A：动作集合。
- P：状态转移矩阵。
- R：奖励函数。reward function。R(s_t=s, a_t=a)
- \gama: 折扣因子。

### MDP + policy
- 基于policy的状态转移矩阵
- 基于policy的reward函数。
- 如何迭代求policy?



