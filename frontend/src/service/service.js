import store from "../store/index";

export const login = async (username, password) => {
  let formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  return await fetch(`${process.env.VUE_APP_API_BASE_URL}/api/token/`, {
    method: "POST",
    body: formData,
    mode: "cors",
  });
};

export const register = async (
  username,
  password,
  name,
  email,
  gender,
  date_of_birth
) => {
  let formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);
  formData.append("name", name);
  formData.append("email", email);
  formData.append("gender", gender);
  formData.append("date_of_birth", date_of_birth);

  return await fetch(`${process.env.VUE_APP_API_BASE_URL}/register/`, {
    method: "POST",
    body: formData,
    mode: "cors",
  });
};

export const appoint = async (
  username,
  password,
  name,
  email,
  gender,
  date_of_birth,
  biography,
  profile_picture,
  teacher_type
) => {
  let formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);
  formData.append("name", name);
  formData.append("email", email);
  formData.append("gender", gender);
  formData.append("date_of_birth", date_of_birth);
  formData.append("biography", biography);
  formData.append("profile_picture", profile_picture);
  formData.append("teacher_type", teacher_type);

  return await fetch(`${process.env.VUE_APP_API_BASE_URL}/appoint/`, {
    method: "POST",
    body: formData,
    mode: "cors",
  });
};


export const get = async (api_url) => {
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    method: "GET",
    mode: "cors",
    headers: { Authorization: `Bearer ${credentials.access_token}` },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      method: "GET",
      mode: "cors",
      headers: { Authorization: `Bearer ${credentials.access_token}` },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const del = async (api_url) => {
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    method: "DELETE",
    mode: "cors",
    headers: { Authorization: `Bearer ${credentials.access_token}` },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      method: "DELETE",
      mode: "cors",
      headers: { Authorization: `Bearer ${credentials.access_token}` },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const post = async (api_url, data) => {
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    body: JSON.stringify(data),
    method: "POST",
    mode: "cors",
    headers: {
      Authorization: `Bearer ${credentials.access_token}`,
      "Content-Type": "application/json",
    },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      body: JSON.stringify(data),
      method: "POST",
      mode: "cors",
      headers: {
        Authorization: `Bearer ${credentials.access_token}`,
        "Content-Type": "application/json",
      },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const multipart_post = async (api_url, data) => {
  let formData = new FormData();
  for (const [key, value] of Object.entries(data)) {
    formData.append(key, value);
  }
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    body: formData,
    method: "POST",
    mode: "cors",
    headers: {
      Authorization: `Bearer ${credentials.access_token}`,
    },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      body: formData,
      method: "POST",
      mode: "cors",
      headers: {
        Authorization: `Bearer ${credentials.access_token}`,
      },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const multipart_patch = async (api_url, data) => {
  let formData = new FormData();
  for (const [key, value] of Object.entries(data)) {
    formData.append(key, value);
  }
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    body: formData,
    method: "PATCH",
    mode: "cors",
    headers: {
      Authorization: `Bearer ${credentials.access_token}`,
    },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      body: formData,
      method: "PATCH",
      mode: "cors",
      headers: {
        Authorization: `Bearer ${credentials.access_token}`,
      },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const put = async (api_url, data) => {
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    body: JSON.stringify(data),
    method: "PUT",
    mode: "cors",
    headers: {
      Authorization: `Bearer ${credentials.access_token}`,
      "Content-Type": "application/json",
    },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      body: JSON.stringify(data),
      method: "PUT",
      mode: "cors",
      headers: {
        Authorization: `Bearer ${credentials.access_token}`,
        "Content-Type": "application/json",
      },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const patch = async (api_url, data) => {
  let credentials = store.getters["global/getCredentials"];
  let response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
    body: JSON.stringify(data),
    method: "PATCH",
    mode: "cors",
    headers: {
      Authorization: `Bearer ${credentials.access_token}`,
      "Content-Type": "application/json",
    },
  });
  if (response.status == 401) {
    await store.dispatch("global/extendLogin");
    credentials = store.getters["global/getCredentials"];
    response = await fetch(`${process.env.VUE_APP_API_BASE_URL}${api_url}`, {
      body: JSON.stringify(data),
      method: "PATCH",
      mode: "cors",
      headers: {
        Authorization: `Bearer ${credentials.access_token}`,
        "Content-Type": "application/json",
      },
    });
    if (response.status == 401) {
      await store.dispatch("global/logout");
    }
  }
  return response;
};

export const extendLogin = async (refresh) => {
  let formData = new FormData();
  formData.append("refresh", refresh);

  return await fetch(`${process.env.VUE_APP_API_BASE_URL}/api/token/refresh/`, {
    method: "POST",
    body: formData,
    mode: "cors",
  });
};
