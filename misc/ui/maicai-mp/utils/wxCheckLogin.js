import { getUserInfo } from '../api/user'

const wxUserProfile = () => new Promise((resolve, reject) => {
    wx.getUserProfile({
        desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
        success: (res) => {
            // console.log("get wechat profile success", res)
            let data = {
                userInfo: res.userInfo,
                hasUserInfo: true
            }
            // wx.setStorageSync('token', data.token)
            resolve(data)
        },
        fail (err) {
            console.log('login error')
            console.log('登录失败！' + err)
            reject(err)
        }
    })
//   wx.login({
//     success (res) {
//       console.log('login success')
//       if (res.code) {
//         // getWechatProfile()
//         getUserInfo({ code: res.code }).then(({ data }) => {
//           console.log('login res', data)
//           wx.setStorageSync('token', data.token)
//           resolve(data)
//         }).catch(err => {
//           console.log('login err', err)
//           wx.clearStorageSync()
//           reject(err)
//         })
//       } else {
//         console.log('登录失败！' + res.errMsg)
//         reject(res)
//       }
//     },
//     fail (err) {
//       console.log('login error')
//       console.log('登录失败！' + res)
//       reject(err)
//     }
//   })
})

const wxLogin = () => new Promise((resolve, reject) => {
    wx.login({
        success (res) {
            console.log("wxlogin succ", res)
            resolve(res)
        },
        fail (err) {
            console.log('登录失败！' + res)
            reject(err)
        }
    })
})

const wxCheckSession = () => new Promise((resolve, reject) => {
  wx.checkSession({
    success (data) {
        console.log("checkSession succ", data)
        resolve(data)
      //session_key 未过期，并且在本生命周期一直有效
    //   if (wx.getStorageSync('token')) {
    //     resolve(wx.getStorageSync('token'))
    //   } else {
    //     wxLogin().then(res => {
    //       resolve(res)
    //     }).catch(err => {
    //       reject(err)
    //     })
    //   }
      // resolve(wx.getStorageSync('token'))
    },
    fail () {
      console.log('checkLogin expired, need login')
      // session_key 已经失效，需要重新执行登录流程
      wxLogin().then(res => { //重新登录
        resolve(res)
      }).catch(err => {
        reject(err)
      })
    }
  })
})

module.exports = {
  wxCheckSession: wxCheckSession,
  wxLogin: wxLogin,
  wxUserProfile: wxUserProfile,
}
