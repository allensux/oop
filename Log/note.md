# Log
- logging模块的处理流程
    - 四大组件：
        - 日志器（loggers）：产生日志的一个接口
        - 处理器（Handler）：把产生的日志发送到相应的目的地
        - 过滤器（filters）：更细的控制那些日志输出
        - 格式器（formatters）：对输出信息格式化