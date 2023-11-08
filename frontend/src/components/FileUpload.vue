<template>
  <div>
    <h1>File Upload</h1>
    <input type="file" @change="handleFileChange">
    <button @click="uploadFile">Upload</button>
    <div v-if="message">{{ message }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      message: null,
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.selectedFile);

      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
        .then(response => response.json())
        .then(data => {
          this.message = data.message;
        })
        .catch(error => {
          this.message = 'Error uploading the file.';
        });
    },
  },
};
</script>
