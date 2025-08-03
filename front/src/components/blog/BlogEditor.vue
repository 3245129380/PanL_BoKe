<template>
  <div class="blog-editor">
    <el-form 
      :model="blogData" 
      :rules="rules" 
      ref="blogForm" 
      label-position="top"
    >
      <el-form-item label="标题" prop="title">
        <el-input 
          v-model="blogData.title" 
          placeholder="请输入博客标题"
          clearable
        />
      </el-form-item>
      
      <el-form-item label="作者" prop="author">
        <el-input 
          v-model="blogData.author" 
          placeholder="请输入作者姓名"
          clearable
        />
      </el-form-item>
      
      <el-form-item label="标签">
        <el-select 
          v-model="blogData.tags" 
          multiple 
          filterable 
          allow-create 
          default-first-option
          placeholder="请选择或输入标签"
        >
          <el-option
            v-for="tag in commonTags"
            :key="tag"
            :label="tag"
            :value="tag"
          />
        </el-select>
      </el-form-item>
      
      <el-form-item label="内容" prop="content">
        <el-tabs v-model="activeTab">
          <el-tab-pane label="编辑" name="edit">
            <el-input
              v-model="blogData.content"
              type="textarea"
              :rows="15"
              placeholder="请输入博客内容，支持Markdown语法"
            />
          </el-tab-pane>
          <el-tab-pane label="预览" name="preview">
            <div class="markdown-preview" v-html="previewContent"></div>
          </el-tab-pane>
        </el-tabs>
      </el-form-item>
      
      <el-form-item>
        <el-button 
          type="primary" 
          @click="submitForm" 
          :loading="submitting"
        >
          {{ submitText }}
        </el-button>
        <el-button @click="cancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue'
import { renderMarkdown } from '../../utils/markdown'

export default {
  name: 'BlogEditor',
  props: {
    initialData: {
      type: Object,
      default: () => ({
        title: '',
        author: '',
        tags: [],
        content: ''
      })
    },
    submitting: {
      type: Boolean,
      default: false
    },
    submitText: {
      type: String,
      default: '发布'
    }
  },
  emits: ['submit', 'cancel'],
  setup(props, { emit }) {
    const blogForm = ref(null)
    const activeTab = ref('edit')
    
    const blogData = reactive({
      title: props.initialData.title || '',
      author: props.initialData.author || '',
      tags: props.initialData.tags || [],
      content: props.initialData.content || ''
    })
    
    // 常用标签
    const commonTags = [
      'Vue', 'React', 'JavaScript', 'TypeScript', 
      'Node.js', 'Python', 'CSS', 'HTML', 
      '前端', '后端', '全栈', '教程'
    ]
    
    // 验证规则
    const rules = {
      title: [
        { required: true, message: '请输入标题', trigger: 'blur' },
        { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'blur' }
      ],
      author: [
        { required: true, message: '请输入作者', trigger: 'blur' },
        { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
      ],
      content: [
        { required: true, message: '请输入内容', trigger: 'blur' }
      ]
    }
    
    // 预览内容
    const previewContent = computed(() => {
      return renderMarkdown(blogData.content)
    })
    
    // 监听初始数据变化
    watch(() => props.initialData, (newVal) => {
      if (newVal) {
        blogData.title = newVal.title || ''
        blogData.author = newVal.author || ''
        blogData.tags = newVal.tags || []
        blogData.content = newVal.content || ''
      }
    }, { deep: true })
    
    // 提交表单
    const submitForm = async () => {
      if (!blogForm.value) return
      
      await blogForm.value.validate((valid) => {
        if (valid) {
          emit('submit', { ...blogData })
        }
      })
    }
    
    // 取消
    const cancel = () => {
      emit('cancel')
    }
    
    return {
      blogForm,
      activeTab,
      blogData,
      commonTags,
      rules,
      previewContent,
      submitForm,
      cancel
    }
  }
}
</script>

<style scoped>
.blog-editor {
  padding: 1.5rem;
}

.markdown-preview {
  padding: 1.5rem;
  border: 1px solid #ecf0f1;
  border-radius: 8px;
  min-height: 300px;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.markdown-preview :deep(h1) {
  font-size: 1.75rem;
  margin: 1.5rem 0;
  color: #2c3e50;
}

.markdown-preview :deep(h2) {
  font-size: 1.5rem;
  margin: 1.2rem 0;
  color: #2c3e50;
}

.markdown-preview :deep(h3) {
  font-size: 1.25rem;
  margin: 0.6rem 0;
}

.markdown-preview :deep(p) {
  margin: 0.5rem 0;
  line-height: 1.6;
}

.markdown-preview :deep(code) {
  background-color: #f0f0f0;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-family: monospace;
}

.markdown-preview :deep(pre) {
  background-color: #f0f0f0;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
}

.markdown-preview :deep(pre code) {
  background-color: transparent;
  padding: 0;
}

.markdown-preview :deep(blockquote) {
  border-left: 4px solid #007bff;
  padding: 0.5rem 1rem;
  margin: 1rem 0;
  background-color: #f8f9fa;
}

.markdown-preview :deep(ul), .markdown-preview :deep(ol) {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

.markdown-preview :deep(li) {
  margin: 0.25rem 0;
}

.markdown-preview :deep(img) {
  max-width: 100%;
  height: auto;
}

.markdown-preview :deep(a) {
  color: #007bff;
  text-decoration: none;
}

.markdown-preview :deep(a:hover) {
  text-decoration: underline;
}
</style>