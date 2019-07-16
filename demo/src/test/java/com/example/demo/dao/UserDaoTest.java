package com.example.demo.dao;

import com.example.demo.entity.User;
import org.junit.Ignore;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.List;

import static org.junit.Assert.*;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UserDaoTest {

    @Autowired
    private UserDao userDao;

    @Test
    public void getAllUser() {
        List<User> userList = userDao.getAllUser();
        assertEquals(2, userList.size());
    }

    @Test
    public void getUserById() {
        User user = userDao.getUserById(1);
        assertEquals("超越", user.getUserName());
    }

    @Test
    @Ignore
    public void insertUser() {
    }

    @Test
    @Ignore
    public void updataUser() {
    }

    @Test
    @Ignore
    public void deleteUser() {
    }
}