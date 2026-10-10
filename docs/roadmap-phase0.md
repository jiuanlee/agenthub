# 阶段零任务清单（W1-W8）：云原生从零到熟练

> 目标：把最大的短板（云原生 0 基础）补齐。结束后能在 K8s 上独立交付一套带监控、可弹性伸缩的服务，面试能聊清"Pod 调度失败怎么排查"。
> 时间预算：工作日每天 2h + 周末 4-6h。

---

## W1：Docker 基础与容器化你的第一个服务

### 学习任务
- [ ] 容器原理速成：namespace（隔离什么）+ cgroup（限制什么）+ UnionFS（镜像分层）
  - 推荐：只需理解到"能向面试官讲清容器和虚拟机的区别"的程度
- [ ] Docker 核心命令：build / run / exec / logs / ps / rm / network / volume
- [ ] Dockerfile 语法：FROM / COPY / RUN / ENTRYPOINT vs CMD / ENV / EXPOSE
- [ ] 镜像分层与缓存机制：为什么依赖变动少的层要放前面

### 动手任务
- [ ] 写一个最简单的 Spring Boot Hello 服务（或复用现有项目）
- [ ] 从零写 Dockerfile 把它容器化，本地跑起来并访问成功
- [ ] 实验：改一行代码重新 build，观察哪一层缓存失效

### 产出/验收
- [ ] 能不看文档写出可用的 Dockerfile
- [ ] 能解释：容器删了数据为什么没了？volume 怎么解决？

---

## W2：Docker 进阶与多服务编排

### 学习任务
- [ ] 多阶段构建（Multi-stage build）：编译环境与运行环境分离
- [ ] 镜像瘦身：JRE 基础镜像、distroless、.dockerignore
- [ ] Docker 网络模型：bridge / host / 容器间通信
- [ ] Docker Compose：services / depends_on / networks / volumes / env_file

### 动手任务
- [ ] 用多阶段构建重写 W1 的 Dockerfile，对比镜像大小（目标：从 ~500MB 降到 <200MB）
- [ ] 写一个 docker-compose.yml：Spring Boot + MySQL + Redis 三服务一键启动
- [ ] 实验：服务间通过 service name 互相访问；故意写错依赖顺序观察报错

### 产出/验收
- [ ] 博客素材：《一个 Java 程序员的 Docker 最佳实践清单》
- [ ] 能讲清：为什么生产环境用多阶段构建？镜像里不该放什么（密钥、源码、构建工具）？

---

## W3：K8s 入门与核心概念

### 学习任务
- [ ] K8s 架构全景：Control Plane（apiserver / etcd / scheduler / controller-manager）+ Node（kubelet / kube-proxy / container runtime）
- [ ] 核心对象：Pod / Deployment / ReplicaSet / Service / Namespace
- [ ] YAML 声明式 API 的思维方式：期望状态 vs 当前状态（和 Java 命令式编程的根本差异）
- [ ] kubectl 核心命令：apply / get / describe / logs / exec / delete / explain

### 动手任务
- [ ] 本地搭建集群：kind（推荐）或 minikube
- [ ] 把 W2 的 Spring Boot 服务部署到 K8s：写 Deployment + Service（ClusterIP）
- [ ] 实验 1：手动删除 Pod，观察 ReplicaSet 自动重建
- [ ] 实验 2：把 Service 改成 NodePort，从宿主机访问
- [ ] 实验 3：kubectl exec 进 Pod 排查问题

### 产出/验收
- [ ] 能画出请求从外部进入 Pod 的完整链路
- [ ] 能解释：Deployment 和 ReplicaSet 和 Pod 的关系？为什么一般不直接创建 Pod？

---

## W4：K8s 配置、存储与网络深入

### 学习任务
- [ ] ConfigMap / Secret：配置与密钥管理（对比 Spring Cloud Config / Nacos）
- [ ] Service 三种类型：ClusterIP / NodePort / LoadBalancer
- [ ] Ingress：域名路由、路径转发（类比 Nginx 反向代理）
- [ ] PV / PVC / StorageClass：有状态服务怎么存储
- [ ] 健康检查：livenessProbe / readinessProbe / startupProbe 的区别与误用后果

### 动手任务
- [ ] 给 Spring Boot 服务配 ConfigMap（环境变量方式 + 文件挂载方式各试一次）
- [ ] 部署 MySQL 到 K8s（带 PVC），删除 Pod 验证数据不丢
- [ ] 安装 Ingress Controller（如 ingress-nginx），用域名路径路由到不同服务
- [ ] 实验：故意配错 livenessProbe 路径，观察 Pod 无限重启，用 describe 排查

### 产出/验收
- [ ] 能讲清三个探针的区别，以及"为什么 readiness 失败不会重启 Pod"
- [ ] 能解释 PV/PVC 为什么分两层（关注点分离：管理员供给 vs 用户申请）

---

## W5：K8s 调度、资源与弹性伸缩

### 学习任务
- [ ] 资源管理：requests / limits，CPU 和内存超卖行为差异（OOMKill 是怎么发生的）
- [ ] QoS 等级：Guaranteed / Burstable / BestEffort
- [ ] 调度机制：nodeSelector / 亲和性（affinity）/ 污点与容忍（taint/toleration）
- [ ] HPA：基于 CPU/内存/自定义指标自动扩缩容
- [ ] RBAC：ServiceAccount / Role / RoleBinding（为 AgentHub 多租户打基础）

### 动手任务
- [ ] 给服务配 requests/limits，用压测工具（wrk/JMeter）打到 OOMKill，观察事件
- [ ] 配置 HPA：压测触发自动扩容，停压后观察缩容
- [ ] 实验：给一个节点打污点，观察 Pod 调度行为变化
- [ ] 创建一个只能读 Pod 的 ServiceAccount，用它的 token 调 API 验证权限边界

### 产出/验收
- [ ] **面试必考题通关**：Pod 一直 Pending 怎么排查？（资源不足/污点/亲和性/PVC 未绑定）
- [ ] 能解释 requests 和 limits 分别影响什么（调度 vs 运行时限制）

---

## W6：K8s 发布策略与 CKA 冲刺

### 学习任务
- [ ] 发布策略：RollingUpdate（maxSurge/maxUnavailable）/ Recreate
- [ ] 灰度与回滚：rollout history / undo；金丝雀发布的实现思路
- [ ] Helm：chart 结构、values 模板化、安装/升级/回滚
- [ ] Kustomize：base + overlay 的多环境管理（dev/staging/prod）

### 动手任务
- [ ] 给服务做滚动更新：观察新旧 Pod 交替过程；执行回滚
- [ ] 用 Helm 把 W3-W5 的所有 YAML 改造成 chart（values 抽出镜像 tag、副本数、资源）
- [ ] 或用 Kustomize 组织 dev/prod 两套 overlay（二选一即可，建议都了解）
- [ ] **CKA 决定点**：如果打算考证，本周开始刷题（killer.sh 模拟题）；不考则把时间投入 W7

### 产出/验收
- [ ] 里程碑：W2 的三服务应用，现在能用 Helm 一条命令部署到 K8s，支持滚动升级与回滚
- [ ] 能讲清金丝雀发布在 K8s 里的两种实现（Ingress 权重 / 多 Deployment）

---

## W7：可观测体系（上）—— 指标与日志

### 学习任务
- [ ] Prometheus 架构：Pull 模型、exporter、PromQL 基础（rate / histogram_quantile）
- [ ] Grafana：数据源接入、Dashboard、告警规则
- [ ] Spring Boot 接入 Micrometer → 暴露 /actuator/prometheus
- [ ] 日志方案：Loki + Promtail（轻量）或 EFK（了解即可）
- [ ] RED 指标方法论：Rate / Errors / Duration

### 动手任务
- [ ] 在 K8s 里部署 Prometheus + Grafana（用 kube-prometheus-stack Helm chart）
- [ ] Spring Boot 服务接入 Micrometer，Prometheus 抓取成功
- [ ] 在 Grafana 搭一个 Dashboard：QPS / 错误率 / P95 延迟 / JVM 内存
- [ ] 配置一条告警规则（如错误率 > 5% 触发）

### 产出/验收
- [ ] 能写基础 PromQL：查某个接口过去 5 分钟的 QPS 和 P99
- [ ] 能讲清 RED 和 USE 方法论分别适用于什么

---

## W8：可观测体系（下）—— 链路追踪与阶段验收

### 学习任务
- [ ] OpenTelemetry：Trace / Span / Context 传播；与 Micrometer/SkyWalking 的关系
- [ ] 分布式链路追踪原理：trace-id 如何在 HTTP/MQ 间传递
- [ ] 追踪后端：Tempo / Jaeger（二选一部署）

### 动手任务
- [ ] Spring Boot 服务接入 OpenTelemetry Agent（无侵入方式）
- [ ] 实现"网关 → 服务 A → 服务 B → MySQL"的完整链路追踪
- [ ] 在 Grafana 里打通 Metrics ↔ Traces 跳转
- [ ] **阶段验收项目**：把 W1-W8 的一切串起来——
  - Helm 一键部署三服务应用到 kind 集群
  - 配好 HPA + 探针 + ConfigMap
  - Grafana 有完整监控面板
  - 压测触发扩容，链路追踪可查，告警可触发

### 产出/验收
- [ ] 博客素材：《把一个 Java 微服务应用完整搬上 K8s：从 Dockerfile 到全链路监控》
- [ ] 模拟面试自测：
  1. Pod OOMKilled 怎么定位和预防？
  2. 滚动更新中发现新版本有 bug，怎么办？
  3. 如何在 K8s 里做配置变更且不重启 Pod？（提示：ConfigMap 更新传播机制 + 局限性）

---

## 每周固定动作（贯穿 W1-W8）

- [ ] 每天用 Cursor/Claude Code 辅助学习与排错（积累 AI 原生工作流经验）
- [ ] 每个周末 30min 复盘：本周哪些概念还模糊？记入个人错题本
- [ ] 所有 YAML / Dockerfile / 笔记提交到本仓库 `learning/k8s-lab/` 目录（面试时可展示动手痕迹）

## 常见陷阱提醒

1. **不要陷入教程地狱**：每个主题只看一份教程就动手，做中查
2. **kind 集群够用了**：不要折腾多节点裸金属集群，时间应该花在概念和实操上
3. **CKA 是可选加分项**：如果 W6 评估时间不够，果断放弃，云原生"会用"比"有证"重要
4. **Java 背景是优势不是包袱**：遇到概念就类比（Ingress≈Nginx、ConfigMap≈Nacos、HPA≈线程池动态扩缩），学得会更快
