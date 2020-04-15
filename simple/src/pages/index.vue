<template>
  <div class="wrapper">
    <!-- 左边内容部分 -->
    <div class="index-left">
      <div class="index-left-block">
        <h2>全部产品</h2>
        <template v-for="product in productList">
          <div>
            <h3>{{ product.title }}</h3>
            <ul>
              <li v-for="item in product.list">
                <a v-bind:href="item.url">{{ item.title }}</a>
              </li>
            </ul>
            <div v-if="product.title=='王者男英雄类'"></div>
            <div v-else class="hr"></div>
          </div>
        </template>
      </div>
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li>dadada</li>
        </ul>
      </div>
    </div>
    <!-- 右边内容部分 -->
    <div class="index-right">
      <div style="width:700px;height:300px;margin:20px auto;background:#20B2AA;">将来是用组件代替</div>
      <div class="index-boader-list">
        <div class="index-boader-item">
          <h2>第一个</h2>
          <p>第一个商品描述</p>
          <div class="index-boader-butten">立即购买</div>
        </div>
        <div class="index-boader-item">
          <h2>第二个</h2>
          <p>第二个商品描述</p>
          <div class="index-boader-butten">立即购买</div>
        </div>
        <div class="index-boader-item">
          <h2>第三个</h2>
          <p>第三个商品描述</p>
          <div class="index-boader-butten">立即购买</div>
        </div>
        <div class="index-boader-item">
          <h2>第四个</h2>
          <p>第四个商品描述</p>
          <div class="index-boader-butten">立即购买</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      productList: {
        pc: {
          title: "王者女英雄",
          list: [
            {
              title: "小妲己",
              url: "https://baike.sogou.com/v7056.htm"
            },
            {
              title: "王昭君",
              url:
                "https://baike.sogou.com/v57933.htm?fromTitle=%E7%8E%8B%E6%98%AD%E5%90%9B"
            },
            {
              title: "貂蝉",
              url:
                "https://baike.sogou.com/v18595.htm?fromTitle=%E8%B2%82%E8%9D%89",
              hot: true
            },
            {
              title: "阿珂",
              url:
                "https://baike.sogou.com/v260877.htm?fromTitle=%E9%98%BF%E7%8F%82"
            }
          ]
        },
        app: {
          title: "王者男英雄类",
          list: [
            {
              title: "李白",
              url: "#"
            },
            {
              title: "凯爹",
              url: "#"
            },
            {
              title: "韩信",
              url: "#"
            },
            {
              title: "云中君",
              url: "#"
            }
          ]
        }
      }
    };
  }
};

</script>
<style scoped>
.wrapper {
  display: flex;
}
.index-left {
  width: 30%;
}
.index-right {
  width: 70%;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  border-radius: 5px;
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
.index-boader-list {
  display: flex;
  flex-wrap: wrap;
  margin-top: 20px;
  justify-content: center;
}
.index-boader-item {
  width: 30%;
  height: 125px;
  background: white;
  padding-left: 120px;
  margin-right: 1%;
  box-shadow: 0 0 1px #ddd;
  margin-bottom: 20px;
  border-radius: 0 0 10px 10px;
}
</style>