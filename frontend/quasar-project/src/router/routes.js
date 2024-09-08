const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/DashboardPage.vue') },
      { path: 'agendamentos', component: () => import('pages/AgendamentosPage.vue') },
      { path: 'consultas-dia', component: () => import('pages/ConsultasDiaPage.vue') },
      { path: 'pesquisa', component: () => import('pages/PesquisaClientePage.vue') },
      { path: 'inserir', component: () => import('pages/InserirPacientePage.vue') },
      { path: 'inserir/agendamento', component: () => import('pages/InserirNovaConsultaPage.vue') },
      { path: 'consultas', component: () => import('pages/ConsultasPage.vue') },

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
