## 问题1：执行 git push 时，终端报远端意外挂掉了错误：

```
枚举对象: 35, 完成.
对象计数中: 100% (35/35), 完成.
使用 4 个线程进行压缩
压缩对象中: 100% (30/30), 完成.
写入对象中: 100% (30/30), 341.28 KiB | 976.00 KiB/s, 完成.
总共 30 （差异 10），复用 0 （差异 0）
Connection to github.com closed by remote host.
fatal: 远端意外挂断了
fatal: 远端意外挂断了
```

解决：该问题应该是提交的改动内容大小超过了git设置的Buffer大小，使用下列命令对git的Buffer扩容即可。

```bash
git config http.postBuffer 100000000
git config ssh.postBuffer 100000000
```

## 问题2：Idea使用 Undo Commit，Revert Commit，Drop Commit区别

|               | 是否删除对代码的修改 |    是否删除Commit记录    | 是否会新增Commit记录 |
| :-----------: | :--------: | :----------------: | :-----------: |
|  Undo Commit  |     不会     | 未 Push 会，已 Push 不会 |      不会       |
| Revert Commit |     会      |         不会         |       会       |
|  Drop Commit  |     会      | 未 Push 会，已 Push 不会 |      不会       |
|               |            |                    |               |


### 一、Undo Commit

**适用情况：代码修改完了，已经Commit了，但是还未push，然后发现还有地方需要修改，但是又不想增加一个新的Commit记录。这时可以进行Undo Commit，修改后再重新Commit。**

如果已经进行了Push，线上的Commit记录还是会存在的

简单来说，就是撤销了你Commit的这个动作。详细解释下：

1. 首先，对项目进行了代码修改，然后进行 commit 操作
	![pict1](resource/Pasted%20image%2020241213144223.png)
2. 确认 Commit 之后（未进行push）
   
    ![](resource/Pasted%20image%2020241213150756.png)
    
3. 进行 Undo Commit 操作
   
    ![](resource/Pasted%20image%2020241213150903.png)
    
4. 执行后和未 Commit 之前完全一样
   
    ![](resource/Pasted%20image%2020241213151135.png)
    

### 二、[Revert](https://so.csdn.net/so/search?q=Revert&spm=1001.2101.3001.7020) Commit

**会新建一个 Revert “xxx Commit”的Commit记录，该记录进行的操作是将"xxx Commit"中对代码进行的修改全部撤销掉。**

1. 首先，对项目进行了代码修改，然后进行 commit 操作
   
    ![](resource/Pasted%20image%2020241213151235.png)
    
    Commit 之后：
    
    ![](resource/Pasted%20image%2020241213151248.png)
    
2. 进行 Revert Commit
   
    ![](resource/Pasted%20image%2020241213151349.png)
    
    执行成功后：
    
    可以看到，新增了 Commit 记录【Revert “测试 Revert Commit”】，该记录中将【测试 “Revert Commit”】中对代码进行的修改删除了。
    
    ![](resource/Pasted%20image%2020241213151407.png)
    
    ![](resource/Pasted%20image%2020241213151419.png)
    

### 三、Drop Commit（慎用）

**未push的Commit记录:**

**会删除Commit记录，同时Commit中对代码进行的修改也会全部被删除**

**已push的Commit记录:**

**区别在于线上的Commit记录不会被删除**

1. 修改代码，然后进行 commit
   
    ![](resource/Pasted%20image%2020241213151433.png)
    
    ![](resource/Pasted%20image%2020241213151444.png)
    
2. 进行 drop commit 操作后
   
    commit 记录被删除，代码修改也被删除
    
    ![](resource/Pasted%20image%2020241213151515.png)
    
3. 已 push 的 commit 记录
   
    ![](resource/Pasted%20image%2020241213151525.png)