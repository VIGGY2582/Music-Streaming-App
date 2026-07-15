package com.example.musicapp.auth.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import com.example.musicapp.auth.repository.UserRepository;
import com.example.musicapp.auth.dto.RegisterRequest;
import com.example.musicapp.auth.dto.LoginRequest;
import com.example.musicapp.auth.entity.User;
import java.util.Optional;
import com.example.musicapp.auth.dto.RegisterRequest;
import com.example.musicapp.auth.entity.User;

@Service
public class AuthService {

    @Autowired
    private UserRepository repo;

    @Autowired
    private PasswordEncoder encoder;

    public String register(RegisterRequest request){

        User user = new User();

        user.setUsername(request.getUsername());
        user.setEmail(request.getEmail());

        user.setPassword(
                encoder.encode(
                        request.getPassword()
                )
        );

        repo.save(user);

        return "User Registered";
    }

    public String login(LoginRequest request){
        Optional<User> userOptional = repo.findByEmail(request.getEmail());
        if(userOptional.isPresent()){
            User user = userOptional.get();
            if(encoder.matches(request.getPassword(), user.getPassword())){
                return "Login Successful"; // normally this would return a JWT
            }
        }
        return "Invalid Credentials";
    }
}