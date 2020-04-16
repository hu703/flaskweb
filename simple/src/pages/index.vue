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
          <li v-for="item in newlist">
            <a v-bind:href="item.url">{{ item.title }}</a>
          </li>
        </ul>
      </div>
    </div>
    <!-- 右边内容部分 -->
    <div class="index-right">
      <div style="width:900px;height:300px;margin:20px auto;background:#20B2AA;">将来是用组件代替</div>
      <div class="index-board-list">
        <div class="index-board-item">
          <div class="index-board-item-inner">
            <h2>第一个</h2>
            <p>第一个商品描述</p>
            <div class="index-board-butten">立即购买</div>
          </div>
        </div>

        <div class="index-board-item">
          <div class="index-board-item-inner">
            <h2>第一个</h2>
            <p>第一个商品描述</p>
            <div class="index-board-butten">立即购买</div>
          </div>
        </div>
        <div class="index-board-item">
          <div class="index-board-item-inner">
            <h2>第一个</h2>
            <p>第一个商品描述</p>
            <div class="index-board-butten">立即购买</div>
          </div>
        </div>
        <div class="index-board-item">
          <div class="index-board-item-inner">
            <h2>第一个</h2>
            <p>第一个商品描述</p>
            <div class="index-board-butten">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"; // 引入

export default {
  mounted() {
    axios
      .get("api/getNewList")
      // 请求成功后的代码
      .then(res => {
        console.log(res);
        this.newlist = res.data.list;
      })
      // 出现错误执行的代码
      .catch(error => {
        console.log(error);
      });
    axios
      .get("api/getProductList")
      // 请求成功后的代码
      .then(res => {
        console.log(res);
        this.productList = res.data.list;
      })
      // 出现错误执行的代码
      .catch(error => {
        console.log(error);
      });
  },
  data() {
    return {
      newlist: [
        {
          title: "镜",
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
      ],
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
          last: true,
          list: [
            {
              title: "李白",
              url: "#"
            },
            {
              title: "凯爹",
              url: "#",
              hot: true
            },
            {
              title: "韩信",
              url: "#"
            },
            {
              title: "云中君",
              url: "#",
              hot: true
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
  border-radius: 0 0 10px 10px;
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