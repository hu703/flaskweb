<template>
    <div>
        
        <div class="silder-wrapper" @mouseover='clearInv' @mouseout='runInv'>
            <!-- 四张轮播图 -->
            <div v-show="nowIndex === index" class="silder-item item1" v-bind:class="['item'+[index+1]]" v-for='(imgUrl,index) in sliderImgList' v-bind:key='index'>
                <a href="">
                    <img v-bind:src="imgUrl" alt="" style='width:900px;height:500px'>
                </a>
            </div>
            
            <!-- 上一张 下一张按钮-->
            <a v-on:click="preHandler" class='btn pre-btn' href="javascript:void(0)">&lt;</a>
            <a v-on:click="nextHandler" class='btn next-btn' href="javascript:void(0)">&gt;</a>


            <!-- 下方圆点 -->
            <ul class='silder-dots'>
                <li v-on:click="clickDots(index)" v-for="(item,index) in sliderImgList" v-bind:key="index">{{ index+1 }}</li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return{
            nowIndex:0, // 显示第几张图片 在模板里设置了一个v-show，添加到条件
            // 添加图片需要用到require
            sliderImgList:[
                require('../assets/pic1.jpg'),
                require('../assets/pic2.jpg'),
                require('../assets/pic3.jpg'),
                require('../assets/pic4.jpg'),
            ]
        }
    },
    methods: {
        clickDots(index){       //下面小圆点事件
            this.nowIndex = index
            console.log(this.nowIndex)
        },
        preHandler(){   // 上一张
            this.nowIndex--;
            if(this.nowIndex < 0){
                this.nowIndex = 3
            }
            // console.log(this.nowIndex)
        },
        nextHandler(){      // 下一张可以调用自动轮播
            this.autoPlay()
        }, 
        autoPlay(){     // 自动轮播 
            this.nowIndex++;  
            if(this.nowIndex >3){
                this.nowIndex = 0
            }
        },
        runInv(){   // 移出事件
            this.invId = setInterval(this.autoPlay,1000)// 每隔1000ms调用一次autoPlay
        },
        clearInv(){     // 移入事件
            clearInterval(this.invId) // 清除
        }
    },
    // 调用
    created() {
        this.runInv()  // 因为我们把调用自动轮播写到了runInv里，所以我们在这里可以调用runInv
        
    },
}
</script>
<style scoped>
    .silder-wrapper{
        width: 900px;
        height: 500px;
        background: #5e7c85;
        position: relative;
        margin-top: 15px;
        box-shadow: 0 0 20px #5e7c85;
    }
    .silder-item{
        width: 900px;
        height: 500px #cccccc;
        line-height: 300px;
        text-align: center;
        font-size:40px;
        position:absolute;
    }
    .item1{
        z-index: 100;
    }
    .item2{
        z-index: 90;
    }
    .item3{
        z-index: 80;
    }
    .item4{
        z-index: 70;
    }
    .silder-dots{
        position: absolute;
        right: 50px;
        bottom:20px;
        z-index:200;
    }
    a{
        text-decoration: none;
    }
    .silder-dots li{
        list-style-type: none;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #444444;
        text-align: center;
        line-height: 20px;
        float: left;
        cursor: pointer;
        color: #008080;
        margin: 0 10px;
        opacity: 0.6;
    }
    .btn{
        display: inline-block;
        width: 50px;
        height: 50px;
        color: #000033;
        font-weight: bold;
        font-size:40px;
        text-align: center;
        position: absolute;
        top: 50%;
        margin-top: -25px;
        opacity: 0.6;
        z-index: 300;
    }
    .pre-btn{
        left:10px
    }
    .next-btn{
        right: 10px;
    }
</style>