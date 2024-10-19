# MongoDB-Setup
My personal mongod & mongosh setup instructions.


# MongoDB Installation and Running Instructions

This guide provides step-by-step instructions for installing MongoDB and `mongosh` on **Windows**, **macOS**, and **Linux**, as well as instructions to run MongoDB using predefined directories for data and logs.

---

## Installation

### Windows Installation

1. Download MongoDB from the [MongoDB download page](https://www.mongodb.com/try/download/community).
   - Select **Windows** and download the `.msi` installer.
2. Run the installer, choose **Complete**, and ensure that **MongoDB as a Service** is selected.
3. Install `mongosh` (MongoDB Shell) if it's not included in the installer, from [this link](https://www.mongodb.com/try/download/shell).

4. Verify installation by running:
    ```bash
    mongod --version
    mongosh
    ```

---

### macOS Installation

#### Option 1: Using Homebrew

1. Install Homebrew:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install MongoDB and `mongosh`:
    ```bash
    brew tap mongodb/brew
    brew install mongodb-community@6.0
    brew install mongosh
    ```

3. Start MongoDB:
    ```bash
    brew services start mongodb/brew/mongodb-community
    ```

4. Verify installation:
    ```bash
    mongod --version
    mongosh
    ```

#### Option 2: Manual Installation

1. Download MongoDB from the [MongoDB website](https://www.mongodb.com/try/download/community) and extract the `.tgz` file.

2. Place binaries in `/usr/local/bin` and download `mongosh` [here](https://www.mongodb.com/try/download/shell).

3. Verify installation:
    ```bash
    mongod --version
    mongosh
    ```

---

### Linux Installation

#### Ubuntu/Debian

1. Import MongoDB GPG key:
    ```bash
    curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo tee /etc/apt/trusted.gpg.d/mongodb-server-6.0.asc
    ```

2. Add MongoDB repository:
    ```bash
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
    ```

3. Install MongoDB:
    ```bash
    sudo apt-get update
    sudo apt-get install -y mongodb-org
    ```

4. Start MongoDB:
    ```bash
    sudo systemctl start mongod
    sudo systemctl enable mongod
    ```

5. Install `mongosh`:
    ```bash
    sudo apt install -y mongodb-mongosh
    ```

6. Verify installation:
    ```bash
    mongod --version
    mongosh
    ```

#### RedHat/CentOS

1. Create a repository file:
    ```bash
    echo "[mongodb-org-6.0]
    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/6.0/x86_64/
    gpgcheck=1
    enabled=1
    gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc" | sudo tee /etc/yum.repos.d/mongodb-org-6.0.repo
    ```

2. Install MongoDB:
    ```bash
    sudo yum install -y mongodb-org
    ```

3. Start MongoDB:
    ```bash
    sudo systemctl start mongod
    sudo systemctl enable mongod
    ```

4. Install `mongosh`:
    ```bash
    sudo yum install -y mongodb-mongosh
    ```

5. Verify installation:
    ```bash
    mongod --version
    mongosh
    ```

---

### Common Running Instructions

1. Ensure MongoDB is properly installed on your system.
2. Start the MongoDB server:
    - **Windows**: MongoDB is installed as a service and should run automatically, if not:
      ```bash
      net start MongoDB
      ```
    - **macOS** (Homebrew):
      ```bash
      brew services start mongodb/brew/mongodb-community
      ```
    - **Linux**:
      ```bash
      sudo systemctl start mongod
      sudo systemctl enable mongod
      ```

3. **Connect to MongoDB**:
    Run the `mongosh` shell:
    ```bash
    mongosh
    ```

4. **Stop MongoDB**:
    - **Windows**:
      ```bash
      net stop MongoDB
      ```
    - **macOS** (Homebrew):
      ```bash
      brew services stop mongodb/brew/mongodb-community
      ```
    - **Linux**:
      ```bash
      sudo systemctl stop mongod
      ```

---

### Configurations

The predefined directories for data and logs are already defined in this repository.

Your `mongod.conf` file is set up with these configurations:

```yaml
# Where and how to store data.
storage:
  dbPath: "../Data/db"

# Where to write logging data.
systemLog:
  destination: file
  path: "../Logs/mongod.log"
  logAppend: true

# Network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1

# Process Management
processManagement:
  windowsService:
    serviceName: MongoDB
    displayName: MongoDB

# Security
security:
  authorization: disabled
```

### Passing Config
Running from this repo you can pass the configuration as follows. 

```bash 
mongod --config "./Config/mongod.conf"
```

