
const App = {
  data() {
      return {
          tasks: ['test'],
      }
  },
  compilerOptions: {
      delimiters: ['[[', ']]'],
  },
  methods: {
  },
  created() {
    this.getTasks();
  },
}

Vue.createApp(App).mount('#app')