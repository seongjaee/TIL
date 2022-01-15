# lazy loading

**왜 lazy loading?**

번들러를 이용하여 앱을 제작할 때, JS 번들이 상당히 커져 페이지 로드 시간에 영향.

각 라우트의 컴포넌트들을 별도로 분할하고, 경로를 방문할 때 로드하는 게 효율적!



Vue Router에서 동적 임포트를 제공.

```javascript
// import UserDetails from './views/UserDetails'  대신
const UserDetails = () => import('./views/UserDetails')

const router = createRouter({
	routes: [{ path: '/users/:id', component: UserDetails }],
})
```

> **Note**
>
> routes에 비동기 컴포넌트 사용하지 말 것!
>
> 루트 컴포넌트 안에 비동기 컴포넌트를 사용할 순 있지만,
>
> 루트 컴포넌트 그 자체는 그냥 dynamic imports이다.



같은 루트 아래의 모든 컴포넌트들을 같은 비동기 chunk 내에 두고 싶을 수 있다.

이를 위해 named chunks를 사용해야한다.

```javascript
const UserDetails = () =>
  import(/* webpackChunkName: "group-user" */ './UserDetails.vue')
const UserDashboard = () =>
  import(/* webpackChunkName: "group-user" */ './UserDashboard.vue')
const UserProfileEdit = () =>
  import(/* webpackChunkName: "group-user" */ './UserProfileEdit.vue')
```

</hr>

기본 코드 vue router의 index.js에서 아래와 같은 코드를 볼 수 있다.

```javascript
{
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
```

이런 식으로 코드를 작성하면 브라우저에서 about.js라는 파일을 확인할 수 있다.



vue.config.js 파일을 만들고 그 안에 다음과 같이 코드를 작성한다.

```javascript
module.exports = {
    chainWebpack: config => {
        config.plugins.delete('prefetch');  // prefetch 삭제
    }
}
```

그러면 기본적으로 prefetch가 불가능하게 한다.

그리고 prefetch를 사용하고 싶은 route에 다음과 같이

```javascript
{
    path: '/contact',
    name: 'Contact',
    // component: Contact
    component: () => import(/* webpackChunkName: "contact", webpackPrefetch:true */ '../views/Contact.vue')
  },
```

`webpackPrefetch:true`로 prefetch를 적용할 수도 있다.



**정리하면**

- 접속 빈도가 높은 컴포넌트(사용자가 접속하자마자 접근할만한)는 prefetch 기능을 사용하지 않아야 유리.
  - 최초에 애플리케이션 접속시 한번에 관련 리소스 다운로드해서, 해당 컴포넌트를 접속했을 때 바로 로딩되게 할 수 있음
- 접속 빈도가 낮은 컴포넌트는 prefetch 기능을 사용해야 유리.
  - 컴포넌트에 접속하는 순간에 다운로드하게함.