(module
  ;; Export the function "fibonacci" so it can be called from outside the module
  (export "fibonacci" (func $fibonacci))

  ;; Define the "fibonacci" function
  (func $fibonacci (param $n i32) (result i32)
    ;; Base case: if $n < 2, return 1
    (if (result i32)
      (i32.lt_s
        (local.get $n)     ;; Load the parameter $n
        (i32.const 2)      ;; Compare $n with 2
      )
      (then
        (i32.const 1)      ;; Return 1 if $n < 2
      )
      (else
        ;; Recursive case: return fibonacci(n - 1) + fibonacci(n - 2)
        (i32.add
          ;; Compute fibonacci(n - 2)
          (call $fibonacci
            (i32.sub
              (local.get $n)   ;; Load the parameter $n
              (i32.const 2)    ;; Subtract 2 from $n
            )
          )
          ;; Compute fibonacci(n - 1)
          (call $fibonacci
            (i32.sub
              (local.get $n)   ;; Load the parameter $n
              (i32.const 1)    ;; Subtract 1 from $n
            )
          )
        )
      )
    )
  )
)
