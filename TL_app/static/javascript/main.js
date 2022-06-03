
// https://developer.mozilla.org/ja/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data

// CSRF対策
  const getCookie = (name) => {
    if (document.cookie && document.cookie !== '') {
      for (const cookie of document.cookie.split(';')) {
        const [key, value] = cookie.trim().split('=')
        if (key === name) {
          return decodeURIComponent(value)
        }
      }
    }
}
const csrftoken = getCookie('csrftoken')

// 記事追加
  const addTLE = document.getElementById('add_tle')
  addTLE.addEventListener('submit', (e) => {
    e.preventDefault()
    const url = '{% url "add" %}'
    const post_title = document.getElementById('post_title')
    // URLのクエリパラメータを管理
    const body = new URLSearchParams()
    body.append('title', post_title.value)

    fetch(url, {
      method: 'POST',
      body: body,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'X-CSRFToken': csrftoken,
      },
    })
      .then((response) => {
        // JSON形式に変換
        return response.json()
      })
      .then((response) => {
        // フォームをクリア
        post_title.value = ''
        // 追加するエレメント
        const postArea = document.getElementById('posts')
        const element = Object.assign(document.createElement('div'), { className: 'col-4 mb-3' })
        const element2 = Object.assign(document.createElement('div'), { className: 'card' })
        const element3 = Object.assign(document.createElement('div'), {
          className: 'card-body',
          textContent: response.title,
        })
        element.appendChild(element2)
        element2.appendChild(element3)
        // 最後に追加
        postArea.insertBefore(element, postArea.lastChild.nextSibling)
      })
      .catch((error) => {
        console.log(error)
      })
  })
var $sidebar = document.querySelector('.sidebar')
var $disvisible = document.querySelector('.disvisible')
$disvisible.addEventListener('click', function() {
  $sidebar.classList.toggle('is-hidden')
}) 
