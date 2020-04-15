<template>
  <div>
    <div class="app_head">
      <div class="app_head_inner">
        <img src="./assets/logo.png" alt="">
        <div class="head-nav">
          <ul class='nav-list'>
            <li>登陆</li>
            <li class='pile'>|</li>
            <li>注册</li>
            <li class='pile'>|</li>
            <li>关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="app_content">
      <router-view></router-view>
    </div>
    <div class="app_footer">
      <p>&copy; 1903c - 2020</p>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
html {
overflow-x:auto;
overflow-y:scroll;
}
body, dl, dt, dd, ul, ol, li, pre, form, fieldset, input, p, blockquote, th, td {
font-weight:400;
margin:0;
padding:0;
}
h1, h2, h3, h4, h4, h5 {
margin:0;
padding:0;
}
body {
background-color:#FFFFFF;
color:#666666;
font-family:Helvetica,Arial,sans-serif;
font-size:12px;
padding:0 10px;
text-align:left;
}
select {
font-size:12px;
}
table {
border-collapse:collapse;
}
fieldset, img {
border:0 none;
}
fieldset {
margin:0;
padding:0;
}
fieldset p {
margin:0;
padding:0 0 0 8px;
}
legend {
display:none;
}
address, caption, em, strong, th, i {
font-style:normal;
font-weight:400;
}
table caption {
margin-left:-1px;
}
hr {
border-bottom:1px solid #FFFFFF;
border-top:1px solid #E4E4E4;
border-width:1px 0;
clear:both;
height:2px;
margin:5px 0;
overflow:hidden;
}
ol, ul {
list-style-image:none;
list-style-position:outside;
list-style-type:none;
}
caption, th {
text-align:left;
}
q:before, q:after, blockquote:before, blockquote:after {
content:””;
}
百度（CSS Reset）：
body {
font-family:arial,helvetica,sans-serif;
font-size:13px;
font-size-adjust:none;
font-stretch:normal;
font-style:normal;
font-variant:normal;
font-weight:normal;
line-height:1.4;
text-align:center;
}
body, ul, ol, dl, dd, h1, h2, h3, h4, h5, h6, p, form, fieldset, legend, input, textarea, select, button, th, td {
margin:0;
padding:0;
}
h1, h2, h3, h4, h5, h6 {
font-size:100%;
font-weight:normal;
}
table {
font-size:inherit;
}
input, select {
font-family:arial,helvetica,clean,sans-serif;
font-size:100%;
font-size-adjust:none;
font-stretch:normal;
font-style:normal;
font-variant:normal;
font-weight:normal;
line-height:normal;
}
button {
overflow:visible;
}
th, em, strong, b, address, cite {
font-style:normal;
font-weight:normal;
}
li {
list-style-image:none;
list-style-position:outside;
list-style-type:none;
}
img, fieldset {
border:0 none;
}
ins {
text-decoration:none;
}
《超越css》（CSS Reset）：
/* Normalizes margin,padding */
body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,form,fieldset,input,p,blockquote,th,td { margin:0;padding:0}
/* Normalizes font-size for headers */
h1,h2,h3,h4,h5,h6 { font-size:100%}
/* Removes list-style from lists */
ol,ul { list-style:none }
/* Normalizes font-size and font-weight to normal */
address,caption,cite,code,dfn,em,strong,th,var { font-size:normal; font-weight:normal }
/* Removes list-style from lists */
table { border-collapse:collapse; border-spacing:0 }
/* Removes border from fieldset and img */
fieldset,img { border:0 }
/* Left-aligns text in caption and th */
caption,th { text-align:left }
/* Removes quotation marks from q */
q:before,q:after { content:”}
Eric Meyer（CSS Reset）——推荐：
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, font, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td {
margin: 0;
padding: 0;
border: 0;
outline: 0;
font-size: 100%;
vertical-align: baseline;
background: transparent;
}
body {
line-height: 1;
}
ol, ul {
list-style: none;
}
blockquote, q {
quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
content: ”;
content: none;
}
/* remember to define focus styles! */
:focus {
outline: 0;
}
/* remember to highlight inserts somehow! */
ins {
text-decoration: none;
}
del {
text-decoration: line-through;
}
/* tables still need ‘cellspacing=”0″‘ in the markup */
table {
border-collapse: collapse;
border-spacing: 0;
}
YUI（CSS Reset）：
body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,form,fieldset,input,textarea,p,blockquote,th,td {
margin:0;
padding:0;
}
table {
border-collapse:collapse;
border-spacing:0;
}
fieldset,img {
border:0;
}
address,caption,cite,code,dfn,em,strong,th,var {
font-style:normal;
font-weight:normal;
}
ol,ul {
list-style:none;
}
caption,th {
text-align:left;
}
h1,h2,h3,h4,h5,h6 {
font-size:100%;
font-weight:normal;
}
q:before,q:after {
content:”;
}
abbr,acronym { 
border:0;
}
.app_head{
  background: #363636;
  color: #b2b2b2;
  height: 90px;
  line-height: 90px;
  width: 100%;
}
.app_head_inner{
  width: 1200px;
  height: 90px;
  margin: 0 auto;
}
.app_head_inner img{
  float: left;
  width: 50px;
  margin-top: 20px;
}
.head-nav{
  float:right
}
.head-nav li{
  float: left;
  cursor: pointer;
}
.head-nav .pile{
  padding: 0 10px;
}
.app_footer{
  text-align: center;
  height: 80px;
  line-height: 80px;
  width: 100%;
  background: #e3e4e8;
  margin-top: 30px;
}
.app_content{
  width: 1200px;
  margin: 0 auto;
}
</style>
