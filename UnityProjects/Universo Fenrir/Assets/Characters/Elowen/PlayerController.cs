using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 3.0f;
    private Animator anim;

    void Start()
    {
        anim = GetComponent<Animator>();
    }

void Update()
{
    // 1. LEITURA DIGITAL (Isso ignora o -1 fantasma do GetAxis)
    float moveX = 0;
    float moveZ = 0;

    if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow)) moveZ = 1;
    else if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow)) moveZ = -1;

    if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow)) moveX = 1;
    else if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow)) moveX = -1;

    // 2. O resto do cálculo continua igual
    Vector3 camForward = Camera.main.transform.forward;
    Vector3 camRight = Camera.main.transform.right;

    camForward.y = 0;
    camRight.y = 0;
    camForward.Normalize();
    camRight.Normalize();

    Vector3 movement = (camForward * moveZ + camRight * moveX).normalized;

    // 3. Lógica de movimento
    if (movement.magnitude > 0.1f)
    {
        anim.SetBool("isWalking", true);
        Quaternion targetRotation = Quaternion.LookRotation(movement);
        transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, 0.15f);
        transform.Translate(movement * speed * Time.deltaTime, Space.World);
    }
    else
    {
        anim.SetBool("isWalking", false);
    }

    // Comandos de dança
    if (Input.GetKeyDown(KeyCode.Alpha1)) anim.SetTrigger("hiphop_dance1");
    if (Input.GetKeyDown(KeyCode.Alpha2)) anim.SetTrigger("hiphop_dance2");
}
}
