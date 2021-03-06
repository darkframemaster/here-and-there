#软件工程
## 一 软件工程概述
###1.1 软件危机的表现
* 软件成本日益增长 
* 开发进度难以控制 
* 软件质量差 
* 开发过程无法有效介入和管理
* 代码难以维护等
###软件危机的原因
* 技术原因
	* 软件规模越来越大 
	* 软件复杂度越来越高 
* 管理原因
	* 软件开发缺乏正确的理论指导，过分依靠个人技巧和创造性
	* 对用户需求没有完整准确的认识

###消除软件危机的途径
* 对计算机软件正确认识。
* 推广使用开发软件成功的技术和方法，研究探索更好更有效的技术和方法，消除错误概念和做法。
* 开发和使用更好的软件工具。
* 对于时间、人员、资源等需要引入更加合理的管理措施。
* **软件工程**正是从**技术和管理**两方面研究如何更好地开发和维护计算机软件的一门新兴学科。

###1.2 软件工程
>（IEEE）1968年秋，提出软件工程

1. 将**系统化、规范化、可量化**的工程原则和方法，应用于软件的开发、运行和维护；
2. 软件工程三要素**方法、工具和过程**
3. 对其中方法的理论研究。
###主要目标
高效开发高质量软件，降低开发成本。
###软件工程知识体系指南
**SWEBOK指南的目的是为软件工程学科的范围提供一致的确认。**

###软件工程基本原理 (开发与维护的指导)
1. 用分阶段的生命周期计划严格管理
2. 坚持进行阶段评审
3. 实行严格的产品控制
4. 采用现代程序设计技术
5. 结果应能清楚地审查
6. 开发小组的人员应该少而精
7. 承认不断改进软件工程实践的必要性

###1.3 统一建模语言 UML
####统一建模语言的功能
可视化（Visualization）、规格说明（Specification）、构造（Constructing）和文档化（Documenting）。

####UML的构成(模型)
* 用例图
* 活动图
* 类图
* 对象图
* 顺序图
* 通信图
* 时序图
* 交互概况图
* 组成结构图
* 组件图
* 包图
* 状态机图
* 部署图

####统一建模语言的视图
* 逻辑视图
* 进程视图
* 开发视图
* 物理视图
* 用例视图

###1.4 软件工程三个要素：方法、工具和过程。

###传统开发方法
又称为结构化方法，是一种静态的思想。

>过程：需求分析->规格说明->设计->实现->集成->维护->新的需求->新的规格说明（循环）

###面向对象方法
* 对象作为融合数据及在数据之上的操作行为的统一的软件构件。
* 把所有对象都划分成类(Class)。每个类都定义了一组数据和一组操作。
* 按照父类(或称为基类)与子类(或称为派生类)的关系，把若干个相关类组成一个层次结构的系统(也称为类等级)。在类等级中，下层派生类自动拥有上层基类中定义的数据和操作，称为继承。
* 对象彼此间仅能通过发送消息互相联系－封装性。
####特点
* 面向对象的程序设计语言有**数据抽象、信息屏蔽、继承**等特征
* 面向对象方法学的出发点和基本原则，是**尽可能模拟人类习惯的思维方式。**
* 概念和表示方法上的一致性，阶段间平滑（无缝）过渡。
* 最终产品中的对象与现实世界中的实体相对应，降低了复杂性，提高了可理解性，简化了软件的开发和维护工作。

##二 软件开发过程
###2.1 软件过程与生命周期区别
* 通常生命周期模型要更**一般化**，而软件开发过程则更为**具体化**。
* 生命周期是软件开发的**宏观上**的框架，软件过程则涉及到软件开发的流程等管理**细节**，在框架稳定的前提下允许对软件过程进行裁剪。

###软件生命周期
过程管理主要采用的是一种**“分而治之”**的思想，即将整个软件的生命周期划分成**软件定义、软件开发和运行维护**三个主要的时期。

* 可行性分析与开发计划
* 需求分析
* 软件设计
* 程序编码　
* 软件测试
* 软件维护

###2.2 传统生命周期模型 P13
####瀑布模型
特点：

* 阶段间具有顺序性和依赖性，**文档驱动**
* 推迟实现，不急于编写代码
	* 尽可能的理解和掌握系统需求，
	* 清楚地区分逻辑设计与物理设计，尽可能推迟程序的物理实现。
* 质量保证

问题：

* 不希望有“变化”
* 变化来的越晚，付出的代价越高。
* 设计阶段过多的假设，导致理想化、一厢情愿的东西过多。(用户只参与需求)
* “文档驱动”，静态

####快速原型模型
特点：

* 对系统进行简单和快速的分析，快速构造一个软件原型。
* 用户和开发者在试用或演示原型过程中加强沟通和反馈，获取到用户真正的需求
* 比较适合一个全新的系统开发
* 运用未来系统中需要的新技术，提前测试一些性能上的要求是否能够达到预期。

问题：

* 所选用的开发技术和工具不一定是实际项目的需要。
* 质量一般都比较差

####增量模型
>也称演化模型

特点：

* 把软件产品作为一系列增量构件来设计、编码、集成和测试。
* 每个构件由多个相互作用的模块构成，并且能够完成特定的功能。
* 第一个增量构件往往实现软件的**基本需求**，提供最核心的功能。

####螺旋模型
特点：

* 将**瀑布模型和快速原型**模型结合起来
* 强调了其他模型所忽视的风险分析，特别适合于**大型复杂的系统**。

问题：

* 原型模型可以在一定程度上降低风险，但对有些风险也无能为力。
* 需要专业的风险评估人员。

####喷泉模型
>也称面向对象的生存期模型

特点：

* 喷泉模型是典型的面向对象生命周期模型。
* “喷泉” 体现了面向对象软件开发过程迭代和无缝的特性。
* 为避免喷泉模型的过分无序，把一个线性过程作为总目标。
* **迭代：**逐步求精
* 阶段间没有明显的界限－面向对象的思想保证了各个阶段开发的一致性。

###2.3 敏捷软件模型
敏捷软件开发又称敏捷开发是一种**应对需求快速变化**的软件开发能力。

敏捷开发的组成包括：**极限编程(XP)、Scrum**、精益开发、动态系统开发方法、特征驱动开发、水晶开发等。

####共同特征：
* 迭代式开发
* 增量交付
* 开发团队和用户反馈推动产品开发
* 持续集成
* 开发团队自我管理

####优势
* 精确
* 质量
* 速度
* 丰厚的投资回报率
* 高效的自我管理团队

敏捷开发更适合规模中小、需求变化频繁的系统开发，并且强调团队的作用，所以更适合集中式的开发模式。

###2.4 敏捷开发模型
####2.4.1 极限编程(XP)
* 主要目的是降低需求变化的成本
* 开发流程：编写用户故事、架构规范、实施规划、迭代计划、代码开发、单元测试、验收测试
* 积极接受变化

####原则与做法
* 互动与交流
* 反馈
* 简单
* 勇气
* 团队

####核心做法
* 小规模，频繁的版本发布，短迭代周期
* 测试驱动开发（Test-driven development）
* 结对编程（Pair programming）
* 持续集成（Continuous integration）
* 每日站立会议（Daily stand-up meeting）
* 共同拥有代码（Collative code ownership）
* 系统隐喻（System metaphor）

###2.4.2 Scrum
* **Scrum注重过程，XP注重实践**
* 需求被定义为产品需求积压（product backlogs）
* 开发过程分为多个**冲刺（Sprint）周期**
* 燃尽图（burn down）是一个公开展示的图表，显示当前冲刺中**未完成的数目**

####Scrum的四种角色
* 产品拥有者
* 利益相关者
* 专家
* 团队成员
 
###2.4.3 微软&MSF
* 包括一个集成的整体使用的多个组件：基础原理、模型、准则等
* 比较关键的模型为组队模型和过程模型
* 微软过程模型
	* 构思(Visioning Phase)
	* 计划(Planning Phase)
	* 开发(Developing Phase)
	* 稳定(Stabilizing Phase)
	* 部署(Deployment Phase)
  
###2.5 过程建模
####使用活动图进行过程建模 P24
* UML活动图
* 开始点、结束点
* 动作及执行顺序
* 条件
* 分支、汇聚 {and, or}
* 对象

##三 需求分析
**涉众：**与目标系统相关的一切人和物。

常见的涉众：最终用户，投资者，业务提出者，业务管理者，业务执行着，第三方，开发方，相关的法律法规。

###3.1 通过用例明确系统功能
用例（Use case）又称为是用户故事（User Story），是对需求的深入分析和理解的输出结果。

步骤：

* 识别角色
	* 角色是存在于系统边界之外的与系统发生某些交互的对象
	* 角色可以是人，也可以是其它软件系统
* 寻找用例（动宾结构）
* 用例规约
	* 用例名称
	* 用例编号
	* 包
	* 维护者
	* 版本
	* 简介
	* 参与角色
	* 业务支持者
	* 引用
	* 前置条件
	* 后置条件
	* 基本事件流
	* 备选事件流
	* 关键性
* **用例提炼**
	* 包含关系: 主用例使用时，包含用例无条件发生。
		* 父->子 在箭头上标注《include》 
	* 扩展关系：主用例使用时可能使用到的用例。
		* 子->父 在箭头上标注《extend》 
* 基本事件流和备选事件流的表示
	* 每个用例都可以用用例活动图表示。（活动图中起点有一个，终点可以没有，可以有多个）
	* **并行表示和泳道表示**

需求分析的障碍：

* 隐含的假设
* 笼统的注释
* 模糊的概括
* 迷惑的命名

三种功能性需求：

* 系统功能
* 用户交互
* 接口需求

###3.2 数据流图 课件03_需求分析
* 数据流图(DFD) 描绘信息流和数据从输入移动到输出的过程中所经受的变换。
* 数据流图有四种基本符号：
	* 数据的源点或终点；变换数据的处理；数据存储；数据流。
* 数据流图中的关系符合号：
	* `*`表示并
	* `+`表示或
	* 异或符号
* 数据流图的画法：
	* 信息的流动
	* 信息流不能为动词
	* 实体到实体的信息流动
	* 处理要有输入输出
	* 处理名不能为名词
* 检查：
	* 一致性：分层DFD中不存在矛盾和冲突
		* 父图与子图平衡：即输入输出一致
		* 数据守恒： 一个加工所有输出数据流中的数据，必须能从该加工的输入数据流中直接获得，或者能通过该加工的处理而产生
	* 完整性：分层DFD本身的完整性，即是否有遗漏的数据流、加工等元素
　 

###3.3 非功能性需求
一些利益相关者没有纯功能上的需求，但要满足他们对最终软件产品某些方面的要求，比如开发规范等。

* 质量需求
* 技术性需求
	* 硬件要求
	* 软件平台
	* 运行环境
* 其它交付物
* 合同需求
	* 商业条款
* 规格说明书
	* 技术协议

###3.4 需求说明书
###3.5 需求验证的方法

##四 类的概要设计
类通常可以分为三种，分别是**实体类（Entity Class）、控制类（Control Class）和边界类（接口类）（Boundary Class）**

* 实体类：对应需求中的实体，通常需要永久保存，一般使用数据库表或文件来记录，既包括存储和传递数据的类，还包括操作数据的类。（名词）
* 控制类：用于体现应用程序的执行逻辑，提供相应的业务操作，抽象控制类可以降低界面和数据库之间的耦合度。控制类有时也称为管理类。（动宾）
* 边界类：边界类用于对外部用户与系统之间的交互对象进行抽象，主要包括界面类，如对话框、窗口、菜单等。

###4.1 类图
* 类名
* 成员变量（**属性**）的表示
	* public：+
	* private：-
	* protect：#
	* package：~
	* 表示方法：+/-/# 变量名：变量类型 **（如果加了下划线就是静态的变量）**
* 类的实例 P58
	* 对象是从类实例化后的结果 
	* 对象名：类名**（有下划线）**
	* 赋了值的成员变量，表示方法：变量名=初值
* 类的细化 P59
	* 方法类：加入了方法的类，方法就是函数
		* 表示方法： +/- 函数名（参数）：返回值类型 **（如果加了下划线就是静态的方法）**
	* 管理类：**同类对象**的协调与管理，主要负责对对象的创建、代理访问其它对象的信息等。管理类必须能够提供所管辖所有对象统一的处理方式。
		* 管理类的识别
			* 一般方法：先对所有的用例进行分析，对每个用例对应产生一个管理类，用来对该场景中需要的对象进行管理和协调。
		* 管理类的注意事项  
			* 管理类每次考虑一个任务，只向管理类添加与该任务相关的方法和方法需要的实例变量。
			* 类与类之间尽可能保持较少的联系，这样可以降低接口的数量。
* 设计优化 P62
	* 对于有很大相似之处的两个类，可以使用一个上层类对它们进行泛化
	* 上层类中的变量大多用protect类型
	* 上层类一般是抽象类不能实例化。
	* **枚举类**
	
###4.2 类的关系 P57
* **关联关系**, Association, 静态，类与类之间的一种拥有联系。
	* 表现形式为一条直线
	* 实现形式一般为**类中的成员变量**
* **依赖关系**，Dependency，动态，应避免双向依赖
	* 表现形式为带**箭头的虚线**，箭头**指向被使用者**。  
	* 实现形式：方法的局部变量，方法的参数，对静态方法的调用等。
 
###顺序图&通讯图
* 类图在UML中是一种静态图，因为描述了系统的功能侧面，而基于类图的顺序图可以用来设计对象之间的**动态交互过程**，描述对象之间的过程调用顺序和关系。
* 通过顺序图可以用来**检验类图中说明的功能是否能够实现活动图中描述的功能需求**。
* 怎么画 P63
	1.  确定交互的范围
	2.  确定参与交互的活动者与对象
	3.  确定活动者、对象的生存周期
	4.  确定交互中产生的消息
	5.  细化消息的内容
 
##五 代码生成之道
###单个类的代码实现 P76
静态属性，增加了对象的耦合性，破坏了面向对象的封装性。

方法的参数前的关键字：

* in：表示参数在方法内部是只读的，不会被修改。
* inout：可以被访问，也可以被修改。
* out：只能被修改，和初始值没什么关系。

###5.1 各种关系的实现
###关联关系
###聚合关系
###组合关系
###依赖关系

##六 类的详细设计
###6.1 图形设计工具
* 程序流程图（flowchart）
	* 简单、直观、易于学习
	* 箭头比较随意——不经意间违背结构化程序设计风格
* 盒图（N-S图）
	* 不允许随意跳转
	* 复杂逻辑绘制繁琐
* 问题分析图（PAD）
	

###6.2 表格工具
* 判定表（决策表）
* 判定树（决策树）

###6.3 语言工具
程序设计语言（Programming Design Language, PDL）是一种用来进行详细设计的语言类工具，又称为结构化语言或伪代码。

###6.4 状态图

###6.5 对象约束语言 *OCL 

##七 设计优化
###小规模设计
* KISS（keep it simple and stupid）
* YAGNI（you ani't gonna need it）
* DRY(don't repeat yourself)

* 从来不碰一个运行的系统(never touch a running system)
* 副作用的产生(side effects)
* 昂贵的细节性修改
* 复制-粘贴(don't repeat yourself)

###设计结构的优化：
* 设计类图应能够容易修改
* 设计类模型应能够很容易的进行扩展
* 类模型应以模块的结构进行组织

###7.1 基本的设计原则
1. **接口隔离原则（The Interface Segregation Principle, ISP）**
	* 应尽量使用“接口继承” ，而非“实现继承”
	* 只将需要的操作“暴露”给客户类
2. **依赖倒置原则（Dependency Inversion Principle，DIP）**
	* 应依赖于抽象，而不要依赖具体
3. **开放封闭原则（The Open-Closed Principle, OCP）**
	* 面向对象思想的最高境界，即设计者应给出对于需求变化进行扩展的模块，而永远不需要改写已经实现的内部代码或逻辑。
	* 模块的行为可以被扩展，以需要满足新的需求。
	* 模块的源代码是不允许进行改动的。 
	* OCP是相对的，没有绝对符合OCP的设计
4. **Liskov替换原则（Liskov Substitution Principle, LSP）**
	* 任何出项父类的地方都可以用子类对其进行无条件替换
	* 当子类型替换父类型后不能违反父类型中的前置条件和后置条件，即一个子类型不得具有比父类型更多的限制
5. **单一职责原则（Single Responsibility Principle, SRP）**
	* 设计的类功能应该只有一个，而不应为两个或多个
6. **合成/聚合复用原则（Composite/Aggregate Reuse Principle, CARP）**
	* 尽量使用合成/聚合形式的委托重用，尽量不使用继承重用。
		* 委托重用追求的是对象间的独立性即低耦合
		* 继承重用追求的是对象间应能尽可能的高内聚。

###7.2 模式 & MVC
####模式
* 模式是表示周境（Context）、动机（System of Forces）、解决方案（Solution）三个方面关系的一个规则
* 根据处理问题的粒度不同，从高到低，模式分为3个层次：架构模式（Architectural Pattern）、设计模式（Design Pattern）和实现模式（Implementation Pattern）
	* 架构模式是模式中的最高层次，描述软件系统里的基本的结构组织或纲要，通常提供一组事先定义好的子系统，指定它们的责任，并给出把它们组织在一起的法则和指南。比如N-层架构、MVC架构模式等。
	* 一个架构模式常常可以分解成很多个设计模式的联合使用。设计模式是模式中的第二层次，用来处理程序设计中反复出现的问题，比如GOF总结的23个基本设计模式——Factory Pattern，Observer Pattern等等。
	* 实现模式是最低也是最具体的层次，处理具体到编程语言的问题。比如，类名、变量名、函数名的命名规则以及异常处理的规则等。

####MVC
* MVC，Model-View-Controller模式，能够很好的对设计的灵活性进行解释。
* MVC的核心思想是**将数据本身与其修改的方式以及数据的展现形式进行分离**。
* 模型：业务数据实际的组织与存储。（数据）
* 视图：向外界显示结果。（展现形式）
* 控制器：改变模型中的值。（修改方式）

MVC的使用是通过两个阶段进行的。

* 第一阶段，与MVC模式相关的对象被创建并进行关联；
* 第二阶段，实现对MVC结构的实际使用。

###7.3 设计模式
>模式分三类：创建模式、结构模式、行为模式

* 创建模式：抽象工厂模式、单例模式
* 结构模式：适配器模式、门面模式 、代理者模式
* 行为模式：观察者模式、策略模式、状态模式

* **抽象工厂（Abstract Factory）模式**
	* 主要作用是实现了客户类在创建产品类时引入的耦合
* **单例模式**
	* 单例模式（Singleton）保证了一个类仅有一个实例，并提供一个访问它的全局访问点。
	* 单例模式要求：
		* (1) 类的所有构造方法都为私有的，防止其被外部创建；
		* (2) 提供一个公有的方法获取该类的实例；
		* (3) 类中的实例变量为私有或受保护的。
* **适配器模式（Adapter）**
	* 把一个类的接口变换成客户类所期待的另一种接口，从而使原本因接口原因不匹配而无法一起工作的两个类能够一起工作
	* 适配器一般有两种工作方式：
		* 一种是通过委托的方式
		* 另外一种是通过继承（接口实现）的方式
* **门面模式（Facade）**
	* 要求外部与一个子系统的通信必须通过一个统一的门面对象进行。
	* 每个子系统一般只要求具有一个门面类，而且此门面类只有一个实例，也就是说它是一个单例模式,这个时候的门面类作用相当于前面介绍的适配器，负责对外部请求的转发，并且可以在此基础上进行功能的扩充
	* 门面类虽然具有多种功能，但它每次为外部提供服务的时候一般只涉及其中一类功能，几乎不会做各种功能的联合使用，也就是这些功能多独立变化，不会形成组合在一起形成的多个变化点，因此本质上并不违反单一职责原则的精神
* **代理模式（Proxy）**
	* 用来对有价值（稀缺）资源的管理
	* 它给这些资源对象提供一个代理对象，并由代理对象控制对资源对象的使用，起到中介的作用。
* **观察者模式（Observer）**
	* 义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象
	* 当这个主题对象在状态上发生变化时，会通知所有观察者对象，使它们能够自动更新自己。
	* MVC架构模式在实现上就使用了观察者模式，其中的主题对象就相当于MVC中的模型，观察者对象相当于MVC中的视图。
* **策略模式（Strategy）**
	* 针对一组算法，将每一个算法封装到具有共同接口的独立的类中，从而使得它们可以相互替换。
	* 能够使得算法可以在不影响到客户端的情况下发生变化，而且将算法的行为和环境分开，环境类负责维持和查询行为类，各种算法在具体的策略类中提供。
* **状态模式（State）**
	* 策略模式的一种应用

##八 实现
###8.1 编程风格
* 源程序文档化
	* （1）标识符的命名
	* （2）程序的注释
		* 序言性注释
		* 功能性注释
	* （3）视觉组织 
* 数据说明
	* （1）数据说明的次序应当规范化，使数据属性容易查找，也有利于测试、排错和维护。
* 语句结构
	* （1）不要为了节省空间而把多个语句写在同一行
	* （2）编写程序应首先考虑清晰性，不要刻意追求技巧性，使程序编写的过于紧凑。
	* （3）程序编写得要简单清楚，直截了当地说明程序员的意图
	* （4）除非对效率有特殊的要求，否则程序编写要做到清晰第一，效率第二
	* （5）首先要保证程序正确，然后才要求提高速度
	* （6）尽可能使用库函数
	* （7）避免使用临时变量而使可读性下降
	* （8）尽量用公共过程或子过程去代替重复的功能代码段
	* （9）避免不必要的转移
	* （10）尽量只采用3中基本的控制结构来编写程序
	* （11）尽量少使用“否定”条件的条件语句
	* （12）避免过多的循环嵌套和条件嵌套
	* （13）避免使用过于复杂的条件
	* （14）有出错处理功能
* 输入/输出方法
* 代码分块
	* 变量区
	* 初始化区
	* 系统功能区
* 相同信息的前后一致
* 构思优先于编码
* 步步为营
	

###匈牙利表示法
* c	：Char字符
* n	：Short短整数和整数（表示一个数）
* i	：int整数
* x, y	：Short短整数（通常用于x坐标和y坐标）
* b	：BOOL（整数）
* l	：LONG（长整数）
* fn	函数指针
* s	字符串
* lp	32位指针
* msg	消息
 
###8.2 非功能性需求的实现
* **硬件**是提升性能的手段之一，但算法、资源利用情况等也需考虑和监控（必要时）。
* **质量方面（正确性）的需求**：可测试性、程序结构。
* **安全方面的要求**：传输安全性、数据安全性、操作安全性。（入侵与健壮性）

###8.3 分布式系统
分布系统中存在多个控制点，因为有多个子程序需要同时工作，如操作系统中的进程

* 同步调用
	* 同步调用具有的最大优点是所有的进程相互了解各自在通信过程中所处的状态
	* 同步调用缺点是需要实现相对复杂的同步通信，由于发送方和接收方需要相互等待会使得两个进程在总体上的执行速度变慢。
* 异步调用
	* 异步调用的执行速度通常是比较快的，因为发送方和接收方可以互相独立的工作。	
	* 异步调用容易出问题的地方是当缓冲区满的情况，这时整个系统运行变慢或者信息可生丢失。

###8.4 XML
XML（可扩展标记语言）是由W3C（万维网联盟, World Wide Web Consortium）委员会定义的一种标准化语言，用来**描述数据模型和数据**。

XML的处理方式一般有两种：文档对象模型（DOM）或用于XML的简单API（SAX）

* DOM是复杂对象处理的首选，比如当XML比较复杂的时候，或者当需要随机处理文档中数据的时候。
* SAX则是以流的方式从文档的开始通过每一节点进行移动，以定位一个特定的节点。

###8.5 程序库 openGL & mfc & STL
* 应尽量选取那些使用者较多的函数库
* 没有对库函数直接进行测试的必要
* 要明确是否存在能够满足任务的相关类库，然后再学习其如何使用，只有对相关的类库做到深入的理解，才能认识到类库的不足在哪里
* 有些简短的相似的命名中可能会在编码过程中引入一些问题，使用中应引起注意

###8.6 组件 button lable list等
* 组件可以理解为一种特殊的对象，组件是对**数据和方法**的简单封装。
* 使用组件可以实现**拖放式编程、快速的属性处理以及真正的面向对象的设计**。
* 组件是对类库思想的进一步提升，不是仅提供单一类的功能，而是将某个子应用封装提供使用。
* 组件可以对接口进行实现，从而提供实现了这些接口的一类对象。
* 使用现成的组件来开发应用程序时，组件一般可以工作在两种模式下：**设计时态和运行时态**。
	* 在设计时态下，组件显示在窗体编辑器下的一个窗体中。设计时态下组件的方法不能被调用，组件不能与最终用户直接进行交互操作，也不需要实现组件的全部功能。
	* 在运行状态下，组件工作在一个已经实际运行的应用程序中。组件必须能够正确地将自身表示出来，它需要对方法的调用进行处理并实现与其他组件之间有效的协同工作。
	* 设计时态下所有的组件在窗体中都是可见的，但在运行时态下不一定可见。如Swing中的JTable、JLabel等在运行时态下就可以设置为不可见，但它们均完成了重要的功能。
* **组建的开发**：
	* 设计组件是一项艰苦的工作。对于组件的开发者，组件是**纯粹的代码**
	* 组件的开发一般**不是可视化**的开发过程，而是用C++等工具严格编制代码的工作。
	* 创建组件的最大意义在于**封装重复的工作**，其次是可以**扩充现有组件的功能**。
* **组件的使用**
	* 组件的使用是一个相对轻松的工作，除了可以使用组件提供的大量功能外，还可以对它们进行定制。
	* 组件的定制通常可以通过配置文件的形式进行，常通过一个配置界面，通过交互的方式对组件中需要改动的属性进行指定。
	 
####Java bean组件
>Java领域中也存在具体的组件支持机制，即所谓的Java Bean。类似的还有微软的ActiveX、C#的COM组件等。

组件与系统以及组件之间的通讯一般是按照**观察者模式**的方式进行组织的。

###8.7 框架
* 快速、高效和正确的将很多**原始的工作**积累合成到一个更大粒度的半成品式的系统中
* 程序员只需对它进行必要的参数定制就能够将其打造成符合用户需求的真实系统
* 框架提供一个通用平台，通过接口或者类继承的方式嵌入业务类，从而达到系统定制的目的。
* 组件与框架最主要的差别就是控制权在框架中要进行转移，也就是说框架中的类会去调用那些由用
* 补充实现的对象中的方法，而不会反过来；但这在组件中是会发生的——反射。

###8.8 数据的持久化
数据的持久化存储一般有两类方式：**物理文件**或**数据库系统**。

* 数据库系统的好处在于不同的应用可以在同一时间对同一数据并发的使用，提供了很好的数据共享性和安全性。
* 很多在分布系统中存在的大部分问题都可以通过数据库系统解决。

####文件持久化：
* 直接使用**文件的方式进行数据的持久化**，不同的程序语言提供了不同的技术支持。
* 其中一个基本功能是能够让开发人员将数据以二进制的原始数据形式将数据存储于文件中。
* 基于这个基本的存储功能，可以衍生出更多的方便的文件存储服务。
* 文件的存储方式好处是**可读性比较好**，可以方便的通过手工编辑或者其它的程序进行读取。
* 问题是开发者必须要为每个需要持久化的类编写存储或读入的方法，这是一项很**繁琐的工作**。
* 缺点是存储的文件是二进制形式的，只能由该类所在的应用所识别和读取。
* 而且，当程序中的类发生某些改变时，如增加了一个新的实例变量，再次读取时就会出现问题。
* 为了能够继续从存储的二进制文件中读取数据，必须要通过一个辅助程序将该对象转换为新形式的类型。

####数据库持久化：
* 大数据量的存储一般情况下都要借助数据库系统来进行。
* 新系统开发大多会选择关系型数据库实现对数据的管理。
* 关系型数据库较为明显的缺点是业务存储的模型需要事先在数据库端设计和构建，在数据持久层需要在应用中进行一些程序设计工作以及对象数据与关系型（表格数据）的兼容性处理等。
* 这种阻抗失配（Impendence mismatch）问题的一种解决方式是使用单独的功能软件实现对应用中
* 在的对象与数据库存储过程的自动化管理，即所谓的对象关系映射（OR Mapping）。
* 完成高效管理业务实体类与其持久化形式间的转换，包括事务管理，使开发者专心业务功能开发。

###8.9 领域特定语言
###8.10 模型驱动架构 MDA
**模型驱动架构（MDA）**的基本思想是提供一种**正式的解决方案**，与具体编程语言甚至是架构无关的。使用MDA进行开发的过程，可以分为四个阶段：

* **CIM（Computation Independent Model）**：聚焦于系统环境及需求，但不涉及系统内部的结构与运作细节。
* **PIM（Platform Independent Model）**：聚焦于系统内部细节，但不涉及实现系统的具体平台。
* **PSM（Platform Specific Model）**：聚焦于系统落实于特定具体平台的细节，如**EJB，J2EE或.NET都是一种具体平台**。
* **Coding**：最后程序员依据PSM的UML模型内容，按图施工，编写出适用于特定具体平台的代码。

* MDA的一个具体的应用是在数据库设计工具Power Designer中针对**实体关系图（ERD）的构建**。
* 数据库模型的设计依次分为四个主要的阶段，分别为**概念模型（Conceptual Design Model, CDM）、逻辑模型（Logical Design Model, LDM）、物理模型（Physical Design Model, PDM）和数据库代码**，分别对应为MDA中的**CIM、PIM、PSM和Coding**四个层次。

###十 质量保证
* 测试策略：测试的阶段组织，包括单元测试、集成测试、系统测试。

**测试理论**

* 软件测试的基本原理是根据用户需求的满足情况判断软件的质量情况。
* 测试的通过**并不能用来证明整个系统是正确的**，因为测试数量是有限的，测试内容的选择通常是对系统可能的缺陷进行分类并有针对性的让其表现出来，并不能代表全部可能的情况。
* 可计算性理论中的停机问题告诉我们不可能用一个单独的程序来判定任意程序的执行是否能够终止。

###10.1 断言(Assertation)
* 一般形式：`Assert <Boolean condition>`
* 断言提供对异常进行检查的能力，但只能在开发阶段使用，并且不能替代常规的异常处理
* 断言规定了方法**必须要满足**的条件，即需求的程序特性。
* Java断言指令的扩展：`assert<boolean condition>：<any object>`
* 位于函数尾部的断言可以用来检验是否该方法的计算是期望的结果，或者说可以用来检验计算出的结果是否具有期望的某些属性。
* `assert false;` 这个断言表示永远都不会通过，可将其放置于不应该到达的地方，以确保此处不可达。
* 对断言的使用要确保不会带来任何的副作用，也就是说不会改变实际类的状态。
* 比如，对于以下迭代器iter的断言是不合适的，因为该断言检测后会导致迭代器状态的改变，使其指向了下一个对象。`assert iter.next()!=null;`

###10.2 单元测试
####测试框架Junit
* 基本思想是对不同的测试用例创建与其对应的测试方法，测试用例的执行和评价由JUnit接管。

###系统的可测试性
###等价类测试

##十一 软件开发环境

甘特图：**项目计划**经常使用一种称为甘特图的图形对计划进行清晰的描述，包括**哪些工作包存在哪些依赖、谁工作在哪些工作报上有哪些具体的工作内容、工作包已经完成的比例等**。

CoCoMo模型评估开发成本。

####能力成熟度与过程模型（CMM）
* 级别一初始级：Initial
* 级别二已管理级：Managed
* 级别三已定义级：Defined
* 级别四已量化级：Quantitatively Managed
* 级别五优化级：Optimizing



##附录
1. 白盒测试——按照程序内部的结构测试程序，检验程序中的每条路径是否都能按预定要求正确工作。有两种测试法既逻辑覆盖测试法和路径测试法
2. 黑盒测试——按照程序的功能测试程序，检验与程序功能有关的输入、输出与程序执行是否正确。有四种方法既等价分类法、边界值分析法、错误猜测法和因果图法
3. 内聚——一个模块内部各个元素彼此结合的紧密程度的度量。
4. 耦合——一个软件结构内不同模块之间互连程度的度量。
5. 软件生存周期：一个软件从提出开发要求开始直到该软件报废为止的整个时期。包括：可行性分析和项目开发计划，需求分析，概要设计，详细设计，编码，测试，维护。
6. 需求分析：开发人员准确地理解用户的要求，进行细致的调查分析，将用户非形式的需求陈述转化为完整的需求定义，再由需求定义转换到相应的需求规格说明的过程。


