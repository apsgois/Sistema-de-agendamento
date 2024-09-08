<template>
    <div class="q-pa-md flex flex-center">
      <div class="row items-start q-gutter-md">
        <q-card class="my-card bg-purple text-white">
          <q-card-section>
            <div class="text-h6">Novo Agendamento</div>
          </q-card-section>
          <q-separator />
          <q-card-actions vertical>
            <q-btn flat>Adicionar</q-btn>
          </q-card-actions>
        </q-card>
  
        <q-card class="my-card bg-secondary text-white">
          <q-card-section>
            <div class="text-h6">Consultas do Dia</div>
          </q-card-section>
          <q-separator />
          <q-card-actions vertical>
            <q-btn flat @click="goToConsultasDia">Buscar</q-btn>
          </q-card-actions>
        </q-card>
  
        <q-card class="my-card bg-grey-8 text-white">
          <q-card-section>
            <div class="text-h6">Pesquisar Cliente</div>
          </q-card-section>
          <q-separator />
          <q-card-actions vertical>
            <q-btn flat @click="goToPesquisa">Buscar</q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  function goToAgendamentos() {
    router.push('/agendamentos')
  }
  
  function goToConsultasDia() {
    router.push('/consultas-dia')
  }
  
  function goToPesquisa() {
    router.push('/pesquisa')
  }
  </script>
  <style scoped>
  .my-card {
    width: 250px;
  }
  </style>
  