import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BlogLayout from '../layouts/BlogLayout.vue'
import TestCommentView from '../views/TestCommentView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    component: BlogLayout,
    children: [
      {
        path: '/blogs',
        name: 'blogs',
        component: () => import('../views/BlogListView.vue')
      },
      {
        path: '/blogs/:id',
        name: 'blog-detail',
        component: () => import('../views/BlogDetailView.vue')
      },
      {
        path: '/create',
        name: 'create-blog',
        component: () => import('../views/CreateBlogView.vue')
      },
      {
        path: '/edit/:id',
        name: 'edit-blog',
        component: () => import('../views/EditBlogView.vue')
      },
      {
        path: '/test-comment',
        name: 'test-comment',
        component: () => import('../views/TestCommentView.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router