<template>
  <v-row no-gutters class="mb-8 px-8 rowdiv">
    <v-col
      xs="0"
      sm="0"
      md="0"
      lg="1"
      xl="1"
    >
    </v-col>

    <v-col
      xs="12"
      sm="12"
      md="12"
      lg="10"
      xl="10"
      class="pt-8"
    >
      <div class="text-h3 font-weight-light pb-8 text-center">
        <span id="span">Receitas</span>
      </div>

      <div>
        <v-img
          style="height: 480px;"
          src="https://nutricaodesafras.com.br/wp-content/uploads/2024/02/plantio-de-hortalicas.jpg"
          cover
          class="my-auto"
        >
        </v-img>

        <div>
          <v-divider class="mb-8 mt-8"><span class="font-weight-bold">ESCOLHA SUA RECEITA</span></v-divider>
          
          <div class="text-subtitle-1 font-weight-light pb-8 text-center">
            <span id="span">NAVEGUE POR CATEGORIA</span>
          </div>

          <div>
            <v-row justify="space-around">
              <v-col
                v-for="(category, key) in recipes"
                :key="key"
                cols="16"
                md="6"
              >
                <div
                class="cursor-pointer"
                @click="navigateToCategories(category)"
                >
                  <v-img
                    style="height: 300px;"
                    :src="category.image"
                    cover
                    class="my-auto"
                  >
                  </v-img>
                  
                  <div class="text-h5 mt-2 mb-2 text-center">
                    <span id="span">{{ category.name }}</span>
                  </div>
                </div>
              </v-col>
            </v-row>
          </div>
        </div>
      </div>
    </v-col>

    <v-col
      xs="0"
      sm="0"
      md="0"
      lg="1"
      xl="1"
    >
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios';
import { fetchCategories, getCategoryFromUrl, getRecipeFromUrl} from '@/utils.js'

export default {
  data() {
    return {
      recipes: []
    }
  },
  methods: {
    navigateToCategories(category) {
      this.$router.push({ path: `/categorias/${category.name}` });
    },
    fetchCategories();
    
  },
  mounted() {
    this.fetchCategories();
  }
}
</script>

<style scoped>
#span{
  font-family: 'MyFont';
}
</style>