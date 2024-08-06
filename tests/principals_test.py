from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B


def test_get_teachers(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    assert response.status_code == 200
    assert isinstance(response.json['data'], list)


def test_grade_assignment_empty_grade(client, h_principal):
    """
    failure case: If the grade is empty, it should return a 400 Bad Request status.
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': ''
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_regrade_assignment_id_invalid(client, h_principal):
    """
    failure case: If assignment id is not in DB, it should return a 400 Bad Request status.
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 500,  # Assuming this ID does not exist
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 404