// src/services/AuthServiceProvider.js

export class AuthServiceProvider {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  async register({ username, email, password }) {
    const query = `
    mutation RegisterUser($username: String!, $email: String!, $password: String!) {
        registerUser(username: $username, email: $email, password: $password) {
            token
            user {
                id
                username
                email
            }
        }
    }
`;

    const variables = { username, email, password };

    const response = await fetch("/api/graphql/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({
        query: query,
        variables: variables,
      }),
    });

    const result = await response.json();

    if (response.ok && result.data?.registerUser) {
      return result.data.registerUser
    }

    const errorMessage = result.errors?.[0]?.message || "Registration failed. Please try again";
    throw new Error(errorMessage)
  }

  async login(username, password) {
    const query = `
      mutation Login($username: String, $password: String) {
        tokenAuth(username: $username, password: $password) {
          success
        }
      }
    `;

    const variables = { username, password };

    const response = await fetch(this.apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({ query, variables }),
      credentials: "include",
    });

    const result = await response.json();

    if (response.ok && result.data?.tokenAuth?.success) {
      return { success: true };
    }

    const errorMessage =
      result.errors?.[0]?.message || "Login failed. Please try again.";

    throw new Error(errorMessage);
  }

  async logout() {
    const query = `
      mutation {
        logout {
          success
        }
      }
    `;

    const response = await fetch(this.apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
      credentials: "include",
    });

    const result = await response.json();

    if (response.ok && result.data?.logout?.success) {
      return { success: true };
    }

    throw new Error("Logout failed.");
  }

  async me() {
    const query = `
      query {
        me {
          id
          username
          email
        }
      }
    `;

    const response = await fetch(this.apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
      credentials: "include",
    });

    const result = await response.json();

    if (response.ok && result.data?.me) {
      return result.data.me;
    }

    throw new Error("Not authenticated");
  }
}
