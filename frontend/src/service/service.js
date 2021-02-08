

export const login = async (username, password) => {
    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    console.log(process.env.VUE_APP_API_BASE_URL);

    return await fetch(`${process.env.VUE_APP_API_BASE_URL}/api/token/`, {
        method: "POST", 
        body: formData,
        mode: "cors",
    });
}

 
 