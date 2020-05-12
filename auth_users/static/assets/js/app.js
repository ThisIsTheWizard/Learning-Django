var vue = new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  delimiters: ['[[', ']]'],
  data: {
    title: "SK Computer Training Centre",
    clipped: true,
    miniVariant: true,
    drawer: true,
    fixed: false,
    items: [
      {
        icon: "mdi-apps",
        title: "Dashboard",
        to: "/"
      },
      {
        icon: "mdi-file-table",
        title: "Examination",
        to: "/student/examination"
      },
      {
        icon: "mdi-file-table",
        title: "Certificates",
        to: "/student/certificates"
      },
      {
        icon: "mdi-file-table",
        title: "Curriculumn Vitae",
        to: "/student/curriculumn-vitae"
      },
      {
        icon: "mdi-file-table",
        title: "Others",
        to: "/student/others"
      }
    ]
  }
})