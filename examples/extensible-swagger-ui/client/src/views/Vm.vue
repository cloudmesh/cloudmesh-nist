<template>
  <div class="vm">
    <h1>Virtual Machines</h1>
     <v-tabs color="#fafafa">

        <v-tab v-for="c in clouds"
          @click="setCloud(c.id)"
          :key="c.id">
          {{c.name}}
        </v-tab>

        <v-tab-item 
          v-for="c in clouds"
          :key="c.id">
          <div class="text-xs-center">
              <v-pagination
                v-model="page"
                :length="6"
              ></v-pagination>
            </div>
              <v-container grid-list-xs fluid>
                <v-layout row wrap>
                  <v-flex
                    v-for="v in c.vms"
                    :key="v.id"
                  >
                    <v-card flat tile>
                        <v-card-title primary-title>
                        {{v.name}}
                        </v-card-title>

                    </v-card>
                  </v-flex>
                </v-layout>
              </v-container>

        </v-tab-item>
</v-tabs> 

{{clouds[0].vms.length}}
  
  </div>
</template>

<script>
import Swagger from 'swagger-client'
let _swaggerClient;

export default {

  data(){
    return {
      page: '',
      clouds: [
        { id: 'azure', name: 'Azure', vms: [] },
        { id: 'aws', name: 'AWS', vms: [] },
        { id: 'chameleon', name: 'OpenStack', vms: [] },
      ]
    }
  },

  async mounted(){
    _swaggerClient = await Swagger('http://localhost:8080/api/swagger.json')
    console.log('swagger client', _swaggerClient)
  },

  methods: {
    async setCloud(cloud) {
      const cloudIndex = this.clouds.findIndex(c => c.id === cloud)

      if (!this.clouds[cloudIndex].vms.length) {
          const result = await _swaggerClient.apis.vm.vm_vm_list({cloud: cloud})
          this.clouds[cloudIndex].vms = result.obj
      }
    },

    async getVm(cloud='') {
      console.log('getVm', cloud)
    }

  }
}

</script>
