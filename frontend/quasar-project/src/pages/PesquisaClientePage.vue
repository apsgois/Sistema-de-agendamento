<template>
    <q-page class="q-pa-md">
      <div class="row justify-between items-center">
        <h4>Gestão de Clientes</h4>
        <div class="text-caption">
          {{ currentDate }} Olá usuário
        </div>
      </div>
  
      <q-btn label="Inserir cliente" color="primary" class="q-mb-md" @click="addClient" />
  
      <q-table
        :rows="clients"
        :columns="columns"
        row-key="id"
        flat
        square
        separator="horizontal"
      >
        <template v-slot:body-cell-actions="props">
          <q-td align="center">
            <q-btn icon="edit" flat color="primary" @click="editClient(props.row)" title="Edição do cadastro de pessoa" />
            <q-btn icon="delete" flat color="negative" @click="confirmDelete(props.row)" title="Exclusão do registro" />
            <q-btn icon="event" flat color="secondary" @click="scheduleAppointment(props.row)" title="Realizar um agendamento para o cliente." />
          </q-td>
        </template>
      </q-table>
  
      <q-dialog v-model="deleteDialog">
        <q-card>
          <q-card-section>
            <div class="text-h6">Exclusão de cliente</div>
            <p>Deseja realmente excluir o cliente {{ selectedClient?.name }}?</p>
          </q-card-section>
  
          <q-card-actions align="right">
            <q-btn flat label="Não" color="negative" v-close-popup />
            <q-btn flat label="Sim" color="positive" @click="deleteClient" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-page>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const currentDate = new Date().toLocaleString('pt-BR')
  const deleteDialog = ref(false)
  const selectedClient = ref(null)
  
  const clients = ref([
    { id: 1, name: 'John Due', phone: '(99) 99999-9999', whatsapp: '(99) 99999-9999', birthDate: '00/00/0000' },
    // Adicione mais clientes conforme necessário
  ])
  
  const columns = [
    { name: 'id', required: true, label: '#', align: 'left', field: 'id' },
    { name: 'name', label: 'Nome', align: 'left', field: 'name' },
    { name: 'phone', label: 'Telefone', align: 'left', field: 'phone' },
    { name: 'whatsapp', label: 'Whatsapp', align: 'left', field: 'whatsapp' },
    { name: 'birthDate', label: 'Data de Nascimento', align: 'left', field: 'birthDate' },
    { name: 'actions', label: 'Ações', align: 'center' }
  ]
  
  function addClient() {
    // Função para adicionar novo cliente
  }
  
  function editClient(client) {
    // Função para editar o cliente selecionado
  }
  
  function scheduleAppointment(client) {
    // Função para agendar consulta para o cliente
  }
  
  function confirmDelete(client) {
    selectedClient.value = client
    deleteDialog.value = true
  }
  
  function deleteClient() {
    // Função para excluir o cliente
    deleteDialog.value = false
    selectedClient.value = null
  }
  </script>
  
  <style scoped>
  .q-page {
    max-width: 1200px;
    margin: auto;
  }
  
  .q-table {
    margin-top: 20px;
  }
  </style>
  