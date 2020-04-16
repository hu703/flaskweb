import Mock from 'mockjs'

Mock.mock('/getNewList/',{
    'list|5':[
        {
            url:'@url',
            title:'ctitle(5,20)'
        }
    ]
})