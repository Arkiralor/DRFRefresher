// JS script to hit user api and return the details

const userAction = async () => {
    const response = await fetch('user/all', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'token ' + localStorage.getItem('token')
            }
      }
    );
    const users = await response.json();
    return users;
  }

export default userAction;
