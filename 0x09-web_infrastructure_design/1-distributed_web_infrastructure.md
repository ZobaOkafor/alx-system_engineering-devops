# Distributed Web Infrastructure
A Distributed Web Infrastructure is a 3-server web infrastructure that distributes the components of a website across multiple servers or devices rather than host everything on a single server or device. This can improve the performance and reliability of a website, as well as make it more resilient to outages or attacks. In a distributed web infrastructure, individual components of a website, such as the database, web server, and application server, can be spread across multiple devices, and requests to the website can be routed to the appropriate device based on factors such as the user’s location or the type of request. This can help to improve the speed and scalability of a website, as well as make it more resilient to failure.

# Let's explain some specifics about this infrastructure.
Reasons for including the additional elements:
1.	Second and Third Servers (Redundancy and Fault Tolerance):
- Redundancy: By adding two additional servers, we create redundancy in the system. If one server fails due to hardware malfunction, software crash, or any other issue, the other servers can continue serving requests without interruption.

- Fault Tolerance: The presence of multiple servers improves fault tolerance. Even if one server experiences problems, the overall system remains operational, minimizing downtime and ensuring continuous availability of the website.

2.	Load Balancer (Distributes Traffic Evenly and Ensures High Availability):
- Distributing Traffic Evenly: The load balancer distributes incoming requests across multiple servers, preventing any single server from becoming overloaded. This ensures that each server handles a manageable amount of traffic, optimizing performance and response times.

- Ensures High Availability: By evenly distributing traffic, the load balancer helps ensure high availability of the website. If one server becomes unavailable, the load balancer redirects traffic to the remaining servers, minimizing the impact of server failures on user experience.

3.	Application Server (Separation of Concerns and Scalability):
- Separation of Concerns: Separating the application logic from the web server allows for better organization and management of code. It also enables different teams to work on the front-end (web server) and back-end (application server) components independently, enhancing development efficiency.

- Scalability: Having dedicated application servers enables horizontal scaling, where additional servers can be added to handle increased traffic or workload. This scalability is crucial for accommodating growth in website traffic and ensuring optimal performance during peak usage periods.

4.	Set of Application Files (Redundancy and Fault Tolerance):
- Redundancy: Hosting multiple copies of the application files on different servers ensures redundancy. If one server experiences issues or failures, the other servers can continue serving the application, minimizing downtime and maintaining availability.

- Fault Tolerance: With duplicate copies of the application files distributed across multiple servers, the system becomes more resilient to failures. Even if one server becomes unavailable, the redundant copies ensure that the application remains accessible to users without interruption.

5.	Database (Data Storage and Management):
- Data Storage: The database is essential for storing and managing the website's data, including user information, content, and settings. It provides a centralized repository for accessing and manipulating data, facilitating efficient data retrieval and storage.

- Data Management: The database manages data integrity, consistency, and security. It enforces data constraints, ensures ACID (Atomicity, Consistency, Isolation, Durability) properties, and implements access control mechanisms to protect sensitive information from unauthorized access or modification.

The distribution algorithm the load balancer is configured with and how it works:
- The load balancer is configured with a round-robin distribution algorithm. This algorithm evenly distributes incoming requests among the available servers in a sequential order. When a client sends a request to the load balancer, it forwards the request to one of the available backend servers. The load balancer maintains a list of backend servers that can handle requests. For each new request, the load balancer selects the next server in the list to which it will forward the request. The load balancer cycles through the list of servers in a circular order. After forwarding a request to a server, it moves to the next server in the list for the subsequent request. This process continues indefinitely, creating a "round-robin" distribution pattern. Since each request is distributed sequentially across the available servers, the round-robin algorithm evenly spreads the workload among them. This helps prevent any single server from becoming overloaded while others remain underutilized, ensuring optimal resource utilization and performance.

Is the load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?
Based on the round-robin algorithm, the load balancer enables an Active-Active setup as requests are sequentially distributed among the servers, hence no server is underutilized or overutilized. Below is the difference between an Active-Active setup and an Active-Passive setup.

Active-Active Setup:
- In an Active-Active setup, all backend servers are actively handling incoming requests simultaneously.
- Each server in the pool is capable of processing requests and serving content to users.
- The load balancer distributes incoming requests across all active servers using a load balancing algorithm like round-robin.
- Active-Active setups are typically used to distribute traffic evenly across multiple servers, optimizing resource utilization and scalability.
- It allows for higher throughput and better performance during periods of high traffic, as the workload is distributed across multiple active servers.

Active-Passive Setup:
- In an Active-Passive setup, one server (the active server) actively handles incoming requests, while the other server (the passive server) remains on standby.
- The passive server does not actively participate in serving requests unless the active server fails or becomes unavailable.
- The load balancer continuously monitors the health and availability of the active server. If the active server fails or is unreachable, the load balancer automatically redirects traffic to the passive server.
- Active-Passive setups are often used for failover scenarios, where high availability and reliability are critical. The passive server serves as a backup, ready to take over in case of a failure in the active server.
- While Active-Passive setups provide redundancy and fault tolerance, they may underutilize resources during normal operation since only one server is actively serving requests at a time.

How a database Primary-Replica (Master-Slave) cluster works:
- In a Primary-Replica cluster, the Primary (Master) node handles write operations and replicates data to the Replica (Slave) nodes. Replica nodes handle read operations and can take over if the Primary node fails.

The difference between the Primary node and the Replica node in regard to the application:
- Primary Node: Handles write operations and serves as the authoritative source of data. It ensures data consistency and integrity.
- Replica Node: Replicates data from the Primary node and handles read operations. It's used for scaling read-heavy workloads and provides fault tolerance.

# Issues associated with a Distributed Web Infrastructure:
- SPOF: Single points of failure exist in components such as the load balancer and database.

- Security Issues: Lack of firewall configuration leaves the infrastructure vulnerable to unauthorized access. Additionally, the absence of HTTPS encryption compromises data security during transmission.

- No Monitoring: Without monitoring tools in place, it's challenging to detect and address performance issues, security threats, and system failures proactively. Monitoring is essential for maintaining the health and stability of the infrastructure.

# Conclusion
The three-server web infrastructure improves reliability, scalability, and performance compared to a single web configurations, but it still has limitations regarding security, monitoring, and single points of failure. Implementing measures such as firewall configurations, HTTPS encryption, and monitoring tools are necessary to address these issues and ensure the stability and security of the infrastructure. Additionally, further enhancements like database clustering and redundant load balancers can be considered for increased fault tolerance and performance optimization.
