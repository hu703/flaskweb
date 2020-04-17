<template>
  <div class="wrapper">
    <!-- 左边内容部分 -->
    <div class="index-left">
      <div class="index-left-block">
        <h2>英雄列举</h2>
        <template v-for="product in productList">
          <div>
            <h3>{{ product.title }}</h3>
            <ul>
              <li v-for="item in product.list">
                <a v-bind:href="item.url">{{ item.title }}</a>
                <span class="hot-tag" v-if="item.hot">hot</span>
              </li>
            </ul>
            <div v-if="!product.last" class="hr"></div>
          </div>
        </template>
      </div>
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li v-for="item in newList">
            <a v-bind:href="item.url">{{ item.title }}</a>
          </li>
        </ul>
      </div>
    </div>
    <!-- 右边内容部分 -->
    <div class="index-right">
      <slider-component></slider-component> 
      <div class="index-board-list">
        <div class="index-board-item" v-for='item in boardlist'>
          <div class="index-board-item-inner">
            <h2>{{item.title}}</h2>
            <p>{{item.decoration}}</p>
            <div v-if='item.saleout' class="index-board-butten">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import SliderComponent from '../components/silderComponent'

export default {
  components:{
    SliderComponent
  },
  mounted() {
    axios.get('/')  /* 接口 */
    .then((res) => {      /*请求成功*/  
      console.log(res.data)    /*打印 */
      this.newList = res.data.list
    })
    .catch((error) => {   /* 请求失败 */
      console.log(error)
    });
    // axios.get("api/getProductList")
    //   // 请求成功后的代码
    // .then((res) => {
    //   console.log(res)
    //   this.productList = res.data
    // })
    // // 出现错误执行的代码
    // .catch(error => {
    //   console.log(error);
    // });
    //   axios
    //   .get("api/getBoardList")
    //   // 请求成功后的代码
    //   .then(res => {
    //     console.log(res)
    //     this.boardlist = res.data.list
    //   })
    //   // 出现错误执行的代码
    //   .catch(error => {
    //     console.log(error);
    //   });
  },
  data() {
    return {
      newList:[],
      productList:null,
      boardlist:null
    }
  }
}
</script>
<style scoped>
.wrapper {
  width: 1200px;
  margin: 0 auto;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-right {
  width: 900px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  border-radius: 0 0 10px px;
  box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
  border-bottom: 1px solid #f0f2f5;
  margin-bottom: 20px;
}
.index-left-block h2 {
  background: #008080;
  padding: 10px 15px;
  color: white;
}
.index-left-block h3 {
  font-weight: bolder;
  padding: 0 15px 0 15px;
}
.index-left-block ul {
  padding: 0 15px;
}
.index-left-block li {
  padding: 5px;
  list-style-type: none;
}
a {
  text-decoration: none;
  color: #444;
}
.index-board-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 15px;
}
.index-board-item {
  width: 400px;
  height: 125px;
  background: white;
  box-shadow: 0 0 1px #ddd;
  border-radius: 0 0 10px 10px;
  margin-bottom: 20px;
  padding: 20px;
}
.index-board-item-inner {
  padding-left: 180px;
  height: 125px;
  background-image: url(../assets/logo.png);
  background-repeat: no-repeat;
  background-size: 20%;
}
.index-board-item-inner h2 {
  font-size: 18px;
  font-weight: bolder;
  margin-bottom: 15px;
}
.index-board-item-inner p {
  margin-bottom: 15px;
}
.index-board-butten {
  width: 80px;
  height: 30px;
  background: #00ced1;
  color: white;
  border-radius: 5px;
  text-align: center;
  line-height: 30px;
}
.hot-tag {
  background: #ff6347;
  color: #ddd;
  border-radius: 3px;
  font-size: 15px;
}
</style>