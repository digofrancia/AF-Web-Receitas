import axios from 'axios';

export const fetchCategories =  async function(){
    axios
      .get('http://localhost:8000/api/v1/categories/')
      .then(response => {
        this.recipes = JSON.parse(JSON.stringify(response.data));
        this.getRecipeFromUrl()
        this.finishData()
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  };

export const getCategoryFromUrl= function(path, key) {
    const pathArray = window.location.pathname.split('/');
    const categoryIndex = pathArray.indexOf('receita');
    return pathArray[categoryIndex + 1];
  };

export const getRecipeFromUrl = function() {
    const nameCategory = this.getCategoryFromUrl()
    const pathArray = window.location.pathname.split('/');
    const categoryIndex = pathArray.indexOf(nameCategory);
    const nameRecipe = pathArray[categoryIndex + 1]
    return decodeURIComponent(nameRecipe)
  };


