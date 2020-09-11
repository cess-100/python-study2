var game={
 data:[],//保存所有数字的二维数组
 rn:4, //总行数
 cn:4, //总列数
 state: 0, //游戏当前状态：Running|GameOver
 RUNNING:1,
 GAMEOVER:0,
 score:0, //分数
 isGameOver:function(){//判断游戏状态为结束
  //如果没有满,则返回false
  if(!this.isFull()){
   return false;
  }else{//否则
   //从左上角第一个元素开始，遍历二维数组
   for(var row=0;row<this.rn;row++){
    for(var col=0;col<this.cn;col++){
     //如果当前元素不是最右侧元素
     if(col<this.cn-1){
     // 如果当前元素==右侧元素
      if(this.data[row][col]==
       this.data[row][col+1]){
       return false;
      }
     }
     //如果当前元素不是最下方元素
     if(row<this.rn-1){
     // 如果当前元素==下方元素
      if(this.data[row][col]==
       this.data[row+1][col]){
       return false;
      }
     }
    }
   }return true;
  }
 },
 start:function(){//游戏开始
  this.state=this.RUNNING;
  //找到游戏结束界面，隐藏
  var div=document.getElementById("gameOver");
  div.style.display="none";
  this.data=[//初始化二维数组
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]
  ];
  this.score=0; //重置分数为0
  /*for(var r=0;r<this.rn;r++){
   this.data[r]=[];//向空数组中添加每一行数组
   for(var c=0;c<this.cn;c++){
    //向当前空行数组中加默认元素0
    this.data[r][c]=0;
   }
  }*/
  //在两个随机位置生成2或4
  this.randomNum();
  this.randomNum();
  //将数据更新到页面
  this.updateView();
 },
 isFull:function(){//判断当前数组是否已满
for(var row=0;row<this.rn;row++){//遍历二维数组
 for(var col=0;col<this.cn;col++){
  // 只要发现当前元素==0
  if(this.data[row][col]==0){
   return false;
  }
 }
}
  //(如果循环正常退出)
  return true;
 },
 randomNum:function(){//在随机空位置生成一个数
  if(!this.isFull()){//如果*不*满，才{
   while(true){//循环true
    //0-3随机生成一个行号row
    var row=parseInt(Math.random()*this.rn);
    //0-3随机生成一个列号col
    var col=parseInt(Math.random()*this.cn);
    //如果data[row][col]==0
    if(this.data[row][col]==0){
    // Math.random():<0.5 >=0.5
    //     2  4
    // 随机生成一个数<0.5?2:4，
    // 放入data[row][col]
     this.data[row][col]=
        Math.random()<0.5?2:4;
     break;//退出循环 
    }
   }
  }
 },
 updateView:function(){
//将二维数组中每个格的数字放入前景格中
//遍历二维数组中每个元素,比如:row=2,col=3, 16
for(var row=0;row<this.rn;row++){
 for(var col=0;col<this.cn;col++){
  /*网页中一切元素，属性，文字都是对象*/
  var div=document.getElementById("c"+row+col);
           //"c23"
  var curr=this.data[row][col]; //当前元素值
  //修改div开始标签和结束标签之间的内容
  div.innerHTML=curr!=0?curr:"";
  //修改div的class属性
  div.className=curr!=0?"cell n"+curr:"cell"
  // class
 }
}
 var span=document.getElementById("score");
 span.innerHTML=this.score;
 //判断并修改游戏状态为GAMEOVER
 if(this.isGameOver()){
  this.state=this.GAMEOVER;
  var div=document.getElementById("gameOver");
  var span=document.getElementById("finalScore");
  span.innerHTML=this.score;
 //修改div的style属性下的display子属性为"block"
  div.style.display="block";
 }
 },//updateView方法的结束
 /*实现左移*/
 /*找当前位置右侧，*下一个*不为0的数*/
 getRightNext:function(row,col){
  //循环变量:nextc——>指下一个元素的列下标
  //从col+1开始,遍历row行中剩余元素，<cn结束
  for(var nextc=col+1;nextc<this.cn;nextc++){
  // 如果遍历到的元素!=0
   if(this.data[row][nextc]!=0){
  //  就返回nextc
    return nextc;
   }
  }return -1;//(循环正常退出，就)返回-1
 },
 /*判断并左移*指定行*中的每个元素*/
 moveLeftInRow:function(row){
  //col从0开始，遍历row行中的每个元素，<cn-1结束
  for(var col=0;col<this.cn-1;col++){
  // 获得当前元素下一个不为0的元素的下标nextc
   var nextc=this.getRightNext(row,col);
  // 如果nextc==-1，(说明后边没有!=0的元素了)
   if(nextc==-1){
    break;
   }else{// 否则
  //  如果当前位置==0,
    if(this.data[row][col]==0){
  //   将下一个位置的值，当入当前位置
     this.data[row][col]=
      this.data[row][nextc];
  //   下一个位置设置为0
     this.data[row][nextc]=0;
     col--;//让col退一格，重复检查一次
    }else if(this.data[row][col]==
       this.data[row][nextc]){
  //  否则，如果当前位置==nextc的位置
  //   将当前位置*=2;
     this.data[row][col]*=2;
  //   下一个位置设置为0;
     this.data[row][nextc]=0;
  //   将当前位置的值，累加到score上
     this.score+=this.data[row][col];
    }
   }
  }
 },
 /*移动所有行*/
 moveLeft:function(){
  var oldStr=this.data.toString();
  //循环遍历每一行
  for(var row=0;row<this.rn;row++){
  // 调用moveLeftInRow方法，传入当前行号row
   this.moveLeftInRow(row);
  }//(循环结束后)
  var newStr=this.data.toString();
  if(oldStr!=newStr){
   //调用randomNum()，随机生成一个数
   this.randomNum();
   //调用updateView()，更行页面
   this.updateView();
  }
 },
 moveRight:function(){
  var oldStr=this.data.toString();
  for(var row=0;row<this.rn;row++){
   this.moveRightInRow(row);
  }
  var newStr=this.data.toString();
  if(oldStr!=newStr){
   this.randomNum();
   this.updateView();
  }
 },
 /*判断并右移*指定行*中的每个元素*/
 moveRightInRow:function(row){
  //col从cn-1开始，到>0结束
  for(var col=this.cn-1;col>0;col--){
   var nextc=this.getLeftNext(row,col);
   if(nextc==-1){
    break;
   }else{
    if(this.data[row][col]==0){
     this.data[row][col]=
      this.data[row][nextc];
     this.data[row][nextc]=0;
     col++;
    }else if(this.data[row][col]==
       this.data[row][nextc]){
     this.data[row][col]*=2;
     this.data[row][nextc]=0;
     this.score+=this.data[row][col];
    }
   }
  }
 },
 /*找当前位置左侧，下一个不为0的数*/
 getLeftNext:function(row,col){
  //nextc从col-1开始，遍历row行中剩余元素，>=0结束
  for(var nextc=col-1;nextc>=0;nextc--){
   // 遍历过程中，同getRightNext
   if(this.data[row][nextc]!=0){
    return nextc;
   }
  }return -1;
 },
 /*获得任意位置下方不为0的位置*/
 getDownNext:function(row,col){
  //nextr从row+1开始，到<this.rn结束
  for(var nextr=row+1;nextr<this.rn;nextr++){
   if(this.data[nextr][col]!=0){
    return nextr;
   }
  }return -1;
 },
 /*判断并上移*指定列*中的每个元素*/
 moveUpInCol:function(col){
  //row从0开始，到<rn-1，遍历每行元素
  for(var row=0;row<this.rn-1;row++){
  // 先获得当前位置下方不为0的行nextr
   var nextr=this.getDownNext(row,col);
   if(nextr==-1){ break; // 如果nextr==-1
   }else{// 否则
  //  如果当前位置等于0
    if(this.data[row][col]==0){
  //   将当前位置替换为nextr位置的元素
     this.data[row][col]=
       this.data[nextr][col];
  //   将nextr位置设置为0
     this.data[nextr][col]=0;
     row--;//退一行，再循环时保持原位
    }else if(this.data[row][col]==
       this.data[nextr][col]){
    //  否则，如果当前位置等于nextr位置
  //   将当前位置*=2
     this.data[row][col]*=2;
  //   将nextr位置设置为0
     this.data[nextr][col]=0;
  //   将当前位置的值累加到score属性上
     this.score+=this.data[row][col];
    }
   }
  }
 },
 /*上移所有列*/
 moveUp:function(){
  var oldStr=this.data.toString();
  //遍历所有列
for(var col=0;col<this.cn;this.moveUpInCol(col++));
  var newStr=this.data.toString();
  if(oldStr!=newStr){
   this.randomNum();
   this.updateView();
  }
 },
 /*下移所有列*/
 moveDown:function(){
  var oldStr=this.data.toString();
for(var col=0;col<this.cn;this.moveDownInCol(col++));
  var newStr=this.data.toString();
  if(oldStr!=newStr){
   this.randomNum();
   this.updateView();
  }
 },
 moveDownInCol:function(col){
  //row从this.rn-1，到>0结束，row--
  for(var row=this.rn-1;row>0;row--){
   var nextr=this.getUpNext(row,col);
   if(nextr==-1){
    break;
   }else{
    if(this.data[row][col]==0){
     this.data[row][col]=
       this.data[nextr][col];
     this.data[nextr][col]=0;
     row++;
    }else if(this.data[row][col]==
       this.data[nextr][col]){
     this.data[row][col]*=2;
     this.data[nextr][col]=0;
     this.score+=this.data[row][col];
    }
   }
  }
 },
 /*获得任意位置上方不为0的位置*/
 getUpNext:function(row,col){
  for(var nextr=row-1;nextr>=0;nextr--){
   if(this.data[nextr][col]!=0){
    return nextr;
   }
  }return -1;
 }
}
//onload事件：当页面加载*后*自动执行
window.onload=function(){
 game.start();//页面加载后，自动启动游戏
 //当按键盘按键时，触发移动:
 document.onkeydown=function(){
  //获得事件对象中键盘号：2步
  //事件对象：在事件发生时自动创建
  //   封装了事件的信息
  if(game.state==game.RUNNING){
   //Step1: 获得事件对象
   var e=window.event||arguments[0];
     //IE   DOM标准
   //Step2: 获得键盘号:e.keyCode
   if(e.keyCode==37){
    game.moveLeft();
   }else if(e.keyCode==39){
    game.moveRight();
   }else if(e.keyCode==38){
    game.moveUp();
   }else if(e.keyCode==40){
    game.moveDown();
   }
   //如果按左键，调用moveLeft
   //否则如果按右键，调用moveRight
  }
 }
}