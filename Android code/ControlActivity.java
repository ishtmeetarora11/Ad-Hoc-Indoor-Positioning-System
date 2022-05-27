package com.example.virtualnavigatormajor;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class ControlActivity extends AppCompatActivity {

    FirebaseUser fuser = FirebaseAuth.getInstance().getCurrentUser();
    DatabaseReference reference = FirebaseDatabase.getInstance().getReference().child(fuser.getUid());
    TextView pathTextView;
    TextView followTextView;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_control);

        pathTextView = findViewById((R.id.pathTextView));
        followTextView = findViewById((R.id.followTextView));





        reference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {

                Log.i("SNAPSHOT VAL", "THIS WORKS");
                Log.i("SNAPSHOT VAL", snapshot.toString());


                String path = snapshot.child("Path").getValue().toString();
                pathTextView.setText(path);

            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(ControlActivity.this, "failed", Toast.LENGTH_SHORT).show();
            }
        });



    }
}