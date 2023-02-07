<script setup>
import { computed } from 'vue'
var _CPU_Usage = "",
    _RAM_Used = "",_RAM_Total = "",
    _RAM_Free = "";
    
function xhrRequest(url){
  var xhr = new XMLHttpRequest();
  xhr.open('get', "http://192.168.2.127/"+url, false);
  xhr.send(null);
  return xhr.response;
}
const CPU_Usage = computed(() => {
  return xhrRequest("cpu")
})
const RAM_Free = computed(() => {
  return xhrRequest("ram_free")
})
const RAM_Used = computed(() => {
  return xhrRequest("ram_used")
})
const RAM_Total = computed(() => {
  return xhrRequest("ram_total")
})
</script>

<template>
  <div class="card">
    <div class="icon-box">
      <img src="../assets/cpu.png" class="icon">
    </div>
    <div class="card-information">
      <div class="card-title">CPU</div>
      <div class="card-mainthing">{{ CPU_Usage }} %</div>
    </div>
  </div>
  <div class="card">
    <div class="icon-box">
      <img src="../assets/ram.png" class="icon">
    </div>
    <div class="card-information">
      <div class="card-title">RAM</div>
      <div class="card-mainthing">{{ RAM_Total }} / {{ RAM_Used }} GiB</div>
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
