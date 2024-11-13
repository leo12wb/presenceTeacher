
CREATE TABLE activitiesTeacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    abreviation VARCHAR(10) NOT NULL,
    _description VARCHAR(255) NOT NULL,
    status VARCHAR(25) NOT NULL
);

CREATE TABLE presencesTeacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    _date DATE NOT NULL,
    start_hour TIME
    end_hour TIME
    _status ENUM('Presente', 'Ausente') NOT NULL,
    status VARCHAR(25) NOT NULL
);

CREATE TABLE auxPresencesTeacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacherId INT NULL DEFAULT NULL,
    presencesTeacherId INT NULL DEFAULT NULL,
    
    FOREIGN KEY (presencesTeacherId) REFERENCES presencesTeacher(id),
    status VARCHAR(25) NOT NULL
);

CREATE TABLE activitiesPresencesTeacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    presencesTeacherId INT NULL DEFAULT NULL,
    activitiespresencesTeacherId INT NULL DEFAULT NULL,
    FOREIGN KEY (presencesTeacherId) REFERENCES presencesTeacher(id),
    FOREIGN KEY (activitiespresencesTeacherId) REFERENCES activitiesTeacher(id)
);

CREATE TABLE authToken (
    id SERIAL PRIMARY KEY,
    appId INT NOT NULL,
    token VARCHAR(200) NOT NULL,
    status BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);