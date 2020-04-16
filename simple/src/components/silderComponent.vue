<template>
    <div>
        <!--  @mouseover='clearInv' @mouseout='runInv' -->
        <div class="silder-wrapper">
            <!-- 四张轮播图 -->
            <div class="silder-item item1">1</div>
            <div class="silder-item item2">2</div>
            <div class="silder-item item3">3</div>
            <div class="silder-item item4">4</div>
            <!-- 下方圆点 -->
            <ul class='silder-dots'>
                <li>&lt;</li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li>&gt;</li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    // props:{
    //     inv:{
    //         type:number,
    //         default:1000
    //     }
    // },
    // data() {

    // },
    // methods: {
    //     runInv(){
    //         setInterval(()=>{
                
    //         },this.inv)
    //     },
    //     clearInv(){}
    // },
}
</script>
<style scoped>
    .silder-wrapper{
        width: 900px;
        height: 500px;
        background: chocolate;
        position: relative;
    }
    .silder-item{
        width: 900px;
        height: 500px;
        border:1px solid black;
        line-height: 500px;
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
    }
    .silder-dots li{
        width: 20px;
        height: 15px;
        border-radius: 50%;
        background: white;
        text-align: center;
        line-height: 20px;
        float: left;
        cursor: pointer;
        color: #008080;
        margin: 0 10px;
        opacity: 0.6;
    }
</style>