<template>
  <v-row no-gutters class="mb-8 px-8">
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
      <div v-if="recipes" class="text-h3 font-weight-light pb-8 text-center">
        <span id="span">{{ filteredRecipe.name }}</span>
      </div>

      <div>
        <div v-if="recipes">
          <v-row justify="space-around">
            <v-col
              v-for="key in filteredRecipe.recipes"
              :key="key"
              cols="16"
              md="6"
            >
              <div>
                <v-img
                  style="height: 300px;"
                  :src="key.image"
                  cover
                  class="my-auto cursor-pointer"
                  @click="navigateToReceipt(key.name)"
                ></v-img>
                
                <div class="d-flex">
                  <div class="text-h6 mb-2">
                    <span id="span">{{ key.name }}</span>
                  </div>
                  <v-spacer></v-spacer>
                  <v-rating
                    v-model="key.rate"
                    readonly
                  ></v-rating>
                </div>
              </div>
            </v-col>
          </v-row>
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
      categoryData: null,
      rating: 3,
      recipes: [],
      filteredRecipe: []
    }
  },
  methods: {
    getCategoryFromUrl() {
      const pathArray = window.location.pathname.split('/');
      const categoryIndex = pathArray.indexOf('categorias');
      return pathArray[categoryIndex + 1];
    },
    navigateToReceipt(recipe) {
      const name = this.filteredRecipe.name
      this.$router.push({ path: `/receita/${name}/${recipe}` });
    },
    fetchCategories();
    
    filterRecipe() {
      const categoryName = this.getCategoryFromUrl();
      this.filteredRecipe = this.recipes.find(recipe => recipe.name === categoryName);
    },
  },
  mounted () {
    this.fetchCategories()
  },
}
</script>


<style scoped>
#span{
  font-family: 'MyFont';
}
</style>