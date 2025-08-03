import MarkdownIt from 'markdown-it'
import mdHighlight from 'markdown-it-highlightjs'

const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
}).use(mdHighlight)

export function renderMarkdown(content) {
  return md.render(content)
}

export function sanitizeHTML(html) {
  // A basic sanitization function to prevent XSS attacks
  const div = document.createElement('div')
  div.textContent = html
  return div.innerHTML
}

export default {
  renderMarkdown,
  sanitizeHTML
}