<template>
    <q-page class="q-pa-md">
      <q-form @submit="onSubmit" class="q-gutter-md">
        <h4>Consulta</h4>
  
        <!-- Informações do Cliente -->
        <q-input filled v-model="client.cpf" label="CPF" mask="###.###.###-##" required />
        <q-input filled v-model="client.firstName" label="Nome" required />
        <q-input filled v-model="client.lastName" label="Sobrenome" required />
        <q-input filled v-model="client.birthDate" label="Data de Nascimento" mask="##/##/####" required />
  
        <!-- Aba de Endereço -->
        <q-tabs v-model="tab" class="text-teal" dense>
          <q-tab name="address" label="Endereço" />
          <q-tab name="currentConsultation" label="Consulta Atual" />
          <q-tab name="previousConsultation" label="Consulta Anterior" />
        </q-tabs>
  
        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="address">
            <div class="row q-gutter-sm items-center">
              <q-input
                filled
                v-model="client.address.cep"
                label="CEP"
                mask="#####-###"
                @keyup.enter="fetchAddress(client.address.cep, 'address')"
                class="col"
              />
              <q-btn
                icon="search"
                color="primary"
                round 
                @click="fetchAddress(client.address.cep, 'address')"
              />
            </div>
            <q-input filled v-model="client.address.street" label="Logradouro" required />
            <q-input filled v-model="client.address.number" label="Número" required />
            <q-input filled v-model="client.address.neighborhood" label="Bairro" required />
            <q-select
              filled
              v-model="client.address.state"
              label="Estado"
              :options="states"
              option-label="label"
              option-value="value"
              required
            />
            <q-input filled v-model="client.address.city" label="Cidade" required />
          </q-tab-panel>
  
          <q-tab-panel name="currentConsultation">
            <q-input filled v-model="consultation.currentObservations" label="Observações da Consulta Atual" type="textarea" />
            <q-input filled v-model="consultation.currentImportantPoints" label="Pontos Importantes da Consulta Atual" type="textarea" />
          </q-tab-panel>
  
          <q-tab-panel name="previousConsultation">
            <q-input filled v-model="consultation.previousObservations" label="Observações da Consulta Anterior" type="textarea" />
            <q-input filled v-model="consultation.previousImportantPoints" label="Pontos Importantes da Consulta Anterior" type="textarea" />
          </q-tab-panel>
        </q-tab-panels>
  
        <q-btn type="submit" label="Salvar" color="primary" />
      </q-form>
    </q-page>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { Notify } from 'quasar'
  import { api } from 'boot/axios'
  
  const tab = ref('address')
  
  const client = ref({
    cpf: '',
    firstName: '',
    lastName: '',
    birthDate: '',
    address: {
      cep: '',
      street: '',
      number: '',
      neighborhood: '',
      state: '',
      city: ''
    }
  })
  
  const consultation = ref({
    currentObservations: '',
    currentImportantPoints: '',
    previousObservations: '',
    previousImportantPoints: ''
  })
  
  const states = [
    { label: 'Acre', value: 'AC' },
    { label: 'Alagoas', value: 'AL' },
    { label: 'Amapá', value: 'AP' },
    { label: 'Amazonas', value: 'AM' },
    { label: 'Bahia', value: 'BA' },
    { label: 'Ceará', value: 'CE' },
    { label: 'Distrito Federal', value: 'DF' },
    { label: 'Espírito Santo', value: 'ES' },
    { label: 'Goiás', value: 'GO' },
    { label: 'Maranhão', value: 'MA' },
    { label: 'Mato Grosso', value: 'MT' },
    { label: 'Mato Grosso do Sul', value: 'MS' },
    { label: 'Minas Gerais', value: 'MG' },
    { label: 'Pará', value: 'PA' },
    { label: 'Paraíba', value: 'PB' },
    { label: 'Paraná', value: 'PR' },
    { label: 'Pernambuco', value: 'PE' },
    { label: 'Piauí', value: 'PI' },
    { label: 'Rio de Janeiro', value: 'RJ' },
    { label: 'Rio Grande do Norte', value: 'RN' },
    { label: 'Rio Grande do Sul', value: 'RS' },
    { label: 'Rondônia', value: 'RO' },
    { label: 'Roraima', value: 'RR' },
    { label: 'Santa Catarina', value: 'SC' },
    { label: 'São Paulo', value: 'SP' },
    { label: 'Sergipe', value: 'SE' },
    { label: 'Tocantins', value: 'TO' }
  ]
  
  async function fetchAddress(cep, addressType) {
    try {
      const response = await api.get(`https://viacep.com.br/ws/${cep}/json/`)
      if (response.data.erro) {
        Notify.create({
          type: 'negative',
          message: 'CEP não encontrado'
        })
        return
      }
  
      client.value[addressType].street = response.data.logradouro
      client.value[addressType].neighborhood = response.data.bairro
      client.value[addressType].city = response.data.localidade
      client.value[addressType].state = response.data.uf
    } catch (error) {
      Notify.create({
        type: 'negative',
        message: 'Erro ao buscar o endereço. Verifique o CEP e tente novamente.'
      })
    }
  }
  
  function onSubmit() {
    console.log('Consulta salva:', { client: client.value, consultation: consultation.value })
  }
  </script>
  
  <style scoped>
  .q-page {
    max-width: 800px;
    margin: auto;
  }
  </style>
  