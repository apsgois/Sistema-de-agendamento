<template>
    <q-page class="q-pa-md">
      <q-table
        :rows="consultations"
        :columns="columns"
        row-key="id"
        class="q-mb-md"
      >
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <q-btn
              @click="viewConsultation(props.row)"
              label="Ver Consulta"
              color="primary"
              size="small"
            />
          </q-td>
        </template>
      </q-table>
    </q-page>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  const consultations = ref([
    { id: 1, name: 'João Silva', time: '09:00' },
    { id: 2, name: 'Maria Oliveira', time: '10:30' },
    { id: 3, name: 'Pedro Santos', time: '14:00' }
  ])
  

  const columns = [
    { name: 'name', label: 'Nome', align: 'left', field: row => row.name },
    { name: 'time', label: 'Horário', align: 'left', field: row => row.time },
    { name: 'action', label: '', align: 'center', field: 'action' }
  ]
  
  function viewConsultation(row) {
    //router.push({ name: 'ConsultaPage', params: { id: row.id } })
    router.push('/consultas/' )
  }
  </script>
  
  <style scoped>
  .q-page {
    max-width: 800px;
    margin: auto;
  }
  </style>
  