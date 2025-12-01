.. _procedure_code_review:

*Example content from an SOP outlining the procedure for updating and reviewing code within the Luma Genomics Unit (LGU).*

.. raw:: html 
    
    <hr />

**Procedure**

**1. Overview of the Procedure**

An overview of the procedure is given in the two schematics below. The actions surrounded by a dotted boxed line involve writing and reviewing code, and should be done with reference to the guidelines and supporting documents laid out in Appendix 1.

...

**2. Roles and Actions**

Actions in the process are performed by roles. One person may assume different roles at different stages of the process subject to constraints.

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Role
     - Team members who can assume roles
     - Responsibilities
   * - Reporter
     - Anyone
     - - Identify requirement for new/changed code
       - Open a GitLab issue
       - Describe the requirement in detail
   * - Developer
     - Anyone, but Developer and Reviewer must be different people for an issue
     - - Open development branch on VCS
       - Make changes to code, test, and commit to branch
       - Create merge request on branch
       - Assign agreed reviewer to review merge request
       - Make changes identified by review and commit them to branch
       - Notify reviewer of completion of work
       - (On approval) complete the merge
       - Assign new version/tag to repository
   * - Reviewer
     - Anyone, but Developer and Reviewer must be different people for an issue
     - - Review merge request according to coding standards and guidelines (see Section 1)
       - Describe and categorise proposed improvements to code
       - (When no more improvements to suggest) approve merge request
       - Notify Developer of outcome of review
   * - Team leader
     - Team leader (Lead developer in their absence)
     - - Review outstanding issues on VCS, assigning priority
       - Assign Developers to high‑priority issues
       - Close issues that are low priority or not needed
       - Assign reviewers to open merge requests
