import Mock from 'mockjs'

// Mock.mock(/getNewList/,{
//     'list|5':[{
//         'url':'@url',   // 加@
//         'title':'@ctitle(5,20)'  // 加@c
//     }]
// })
Mock.mock(/getnewList/, {
    'list|5': [{
      'url': '@url',
      'title': '@ctitle(5,20)'
    }]
  })

// Mock.mock(/getProductList/,{
//     pc: {
//         title: "@ctitle(5)",
//         list: [
//         {
//             title: "@ctitle(1,20)",
//             url: "@url"
//         },
//         {
//             title: "@ctitle(1,20)",
//             url: "@url"
//         },
//         {
//             title: "@ctitle(1,20)",
//             url: "@url",
//             hot: '@boolean'
//         },
//         {
//             title: "@ctitle(1,20)",
//             url: "@url"
//         }
//         ]
//     },
//     app: {
//         title: "@ctitle",
//         last: true,
//         list: [
//         {
//             title: "@ctitle(1,20)",
//             url: "@url"
//             },
//             {
//                 title: "@ctitle(1,20)",
//                 url: "@url"
//             },
//             {
//                 title: "@ctitle(1,20)",
//                 url: "@url",
//                 hot: '@boolean'
//             },
//             {
//                 title: "@ctitle(1,20)",
//                 url: "@url"
//             }
//         ]
//     }
// })


// Mock.mock(/getBoardList/,[
//     {
//         title:'@ctitle',
//         description:'@ctitle(8)',
//         saleout:'@boolean'
//     },
//     {
//         title:'@ctitle',
//         description:'@ctitle(8)',
//         saleout:'@boolean'
//     },
//     {
//         title:'@ctitle',
//         description:'@ctitle(8)',
//         saleout:'@boolean'
//     },
//     {
//         title:'@ctitle',
//         description:'@ctitle(8)',
//         saleout:'@boolean'
//     },
// ])
export default Mock
