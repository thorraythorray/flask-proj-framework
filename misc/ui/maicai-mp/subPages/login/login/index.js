import { wxCheckSession, wxUserProfile } from '../../../utils/wxCheckLogin'
import { login } from '../../../api/user'

const app = getApp()
Page({
  data: {
    hasUserInfo: false,
  },
  onLoad () {
    // wxCheckSession().then(({data}) => {
    //     this.setData({
    //         hasUserInfo: true
    //     })
    // }).catch(err => {
    //     this.setData({
    //         hasUserInfo: false
    //     })
    //     console.log(err)
    // })
    // this._eventChannel = this.getOpenerEventChannel()
  },

  getUserProfile(e) {
    wxUserProfile().then(data => {
        console.log(data)
        this.setData({
            userInfo: data.userInfo,
            hasUserInfo: true
        })
    }).catch(err => {
        this.setData({
            hasUserInfo: false
        })
        console.log(err)
    })
  },

//   getUserProfile(e) {
//     // 推荐使用 wx.getUserProfile 获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认
//     // 开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
//     wx.getUserProfile({
//       desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
//       success: (res) => {
//         this.setData({
//           userInfo: res.userInfo,
//           hasUserInfo: true
//         })
//       }
//     })
//   },

  getPhoneNumber ({ detail }) {
    // console.log(detail)
    // await wxCheckSession()
    const ok = detail.errMsg === 'getPhoneNumber:ok'
    if (ok) {
      const { encryptedData, iv } = detail
      login({ encryptedData, iv }).then(({ data }) => {
        const { cartCount, mobile, canGet, points } = data
        Object.assign(app.globalData, { canGet, cartCount, userInfo: { mobile }, points })
        wx.navigateBack()
      })
      // wxCheckSession().then(token => {
      //   // console.log(token)
      //   login({ encryptedData, iv }).then(({ data }) => {
      //     // console.log(data)
      //     const { cartCount, mobile, orderStatusCount, token } = data
      //     wx.setStorageSync('token', token)
      //     Object.assign(app.globalData, { cartCount, orderStatusCount, userInfo: { mobile } })
      //     // this._eventChannel?.emit?.('getLoginInfo')
      //     wx.navigateBack()
      //   })
      // })
    } else {
      wx.showModal({
        title: '授权失败',
        content: '您已拒绝获取微信绑定手机号登录授权，可使用其它手机号验证登录',
        cancelText: '知道了',
        confirmText: '验证登录',
        success (res) {
          if (res.confirm) {
            wx.navigateTo({ url: '/subPages/login/register/index' })
          }
        }
      })
    }
  }
})