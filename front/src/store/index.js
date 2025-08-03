import { createPinia } from 'pinia'
import { useCommentStore } from './comment'

const pinia = createPinia()

// Register stores
export { useCommentStore }

export default pinia