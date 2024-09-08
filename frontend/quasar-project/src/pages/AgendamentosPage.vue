<template>
    <q-page class="q-pa-md">
      <div class="q-gutter-md">
        <h4>Agendamento - {{ patientName }}</h4>
        <q-btn
          label="Adicionar Nova Consulta"
          color="primary"
          icon="add"
          @click="addAppointment"
          class="q-mb-md"
        />

        <q-table
          :rows="appointments"
          :columns="columns"
          row-key="id"
          flat
          dense
          separator="horizontal"
        >
          <template v-slot:body-cell-actions="props">
            <q-btn
              icon="edit"
              color="primary"
              flat
              round
              dense
              @click="editAppointment(props.row)"
            />
            <q-btn
              icon="delete"
              color="negative"
              flat
              round
              dense
              @click="deleteAppointment(props.row)"
            />
            <q-btn
              icon="visibility"
              color="teal"
              flat
              round
              dense
              @click="viewStatus(props.row)"
            />
          </template>
        </q-table>
      </div>
    </q-page>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { Notify } from 'quasar'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const patientName = 'John Doe' 
  const appointments = ref([
    {
      id: 1,
      date: '10/09/2024',
      whatsapp: '(11) 98765-4321',
      status: 'Pendente'
    },
    {
      id: 2,
      date: '01/08/2024',
      whatsapp: '(21) 91234-5678',
      status: 'Realizada'
    }
  ])
  
  const columns = [
    { name: 'date', label: 'Data', align: 'left', field: 'date' },
    { name: 'whatsapp', label: 'WhatsApp', align: 'left', field: 'whatsapp' },
    { name: 'status', label: 'Status', align: 'left', field: 'status' },
    { name: 'actions', label: 'Ações', align: 'center', field: 'actions' }
  ]

  function addAppointment() {
    router.push('/inserir/agendamento')
    Notify.create({
      message: 'Adicionar nova consulta',
      type: 'info'
    })
  }
  
  function editAppointment(appointment) {
    Notify.create({
      message: `Editar agendamento de ${appointment.date}`,
      type: 'info'
    })
  }
  
  function deleteAppointment(appointment) {
   
    const index = appointments.value.findIndex(a => a.id === appointment.id)
    if (index !== -1) {
      appointments.value.splice(index, 1)
      Notify.create({
        message: `Agendamento de ${appointment.date} removido com sucesso`,
        type: 'positive'
      })
    }
  }
  
 
  function viewStatus(appointment) {
  
    Notify.create({
      message: `Visualizando status de ${appointment.date}`,
      type: 'info'
    })
  }
  </script>
  
  <style scoped>
  .q-page {
    max-width: 900px;
    margin: auto;
  }
  </style>
  